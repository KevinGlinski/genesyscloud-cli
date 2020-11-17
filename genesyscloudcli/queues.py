import api_client
import click
import printer
from click.decorators import option

queue_route = "/api/v2/routing/queues"

@click.group()
def queues():
    """Functions to handle Queues"""
    pass

@queues.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Queues"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(queue_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@queues.command()
@click.argument("queue_id")
def get(queue_id):
    """List a specific queue"""
    client = api_client.ApiClient()
    response = client.get(queue_route+"/{}".format(queue_id))
    printer.print_data(response)

        
@queues.command()
@click.argument("queue_id")
def observations(queue_id):
    """Gets observation statistics for a queue"""
    client = api_client.ApiClient()

    query = {
        "filter": {
        "type": "or",
        "predicates": [
        {
            "type": "dimension",
            "dimension": "queueId",
            "operator": "matches",
            "value": "e58f059a-8d02-477d-a0a7-55efcbde7a7a"
        }
        ]
        },
        "metrics": [
            "oInteracting",
            "oWaiting"
        ]
    }
    response = client.post("/api/v2/analytics/queues/observations/query".format(queue_id), query)

    data = []

    for result in response["results"]:
        if 'mediaType' in result['group']:
            elem = {
                'mediaType': result['group']['mediaType']
            }

            for metric in result['data']:
                if metric['metric'] == 'oInteracting':
                    elem['interacting'] = metric['stats']['count']
                elif metric['metric'] == 'oWaiting':
                    elem['waiting'] = metric['stats']['count']
            
            data.append(elem)

    printer.print_data(data)



def register(cli):
    cli.add_command(queues)