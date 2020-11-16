import api_client
import click
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
    return client.get(queue_route)

@queues.command()
@click.argument("queue_id")
def get(queue_id):
    """List a specific queue"""
    client = api_client.ApiClient()
    return client.get(queue_route+"/{}".format(queue_id))


def register(cli):
    cli.add_command(queues)