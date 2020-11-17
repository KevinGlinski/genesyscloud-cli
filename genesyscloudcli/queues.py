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
def list():
    """Listing Queues"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(queue_route)
    
    printer.print_name_id_data(response)

@queues.command()
@click.argument("queue_id")
def get(queue_id):
    """List a specific queue"""
    client = api_client.ApiClient()
    response = client.get(queue_route+"/{}".format(queue_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(queues)