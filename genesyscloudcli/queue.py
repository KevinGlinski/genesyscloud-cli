import api_client
import click
from click.decorators import option

queue_route = "/api/v2/routing/queues"

@click.group()
def queue():
    """Functions to handle Queues"""
    pass

@queue.command()
def list():
    """Listing Queues"""
    client = api_client.ApiClient()
    return client.get(queue_route)

@queue.command()
@option("--queue_id", "-q", required=True, type=str)
def get(queue_id):
    """List specific queue"""
    client = api_client.ApiClient()
    return client.get(queue_route+"/{}".format(queue_id))


def register(cli):
    cli.add_command(queue)