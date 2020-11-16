import api_client
import click
from click.decorators import option

contact_list_route = "/api/v2/outbound/contactlists"

@click.group()
def contact_list():
    """Functions to handle Contact Lists"""
    pass

@contact_list.command()
def list():
    """Listing Contact Lists"""
    client = api_client.ApiClient()
    return client.get(contact_list_route)

@contact_list.command()
@option("--contact_list_id", "-c", required=True, type=str)
def get(contact_list_id):
    """List specific Contact Lists"""
    client = api_client.ApiClient()
    return client.get(contact_list_route+"/{}".format(contact_list_id))


def register(cli):
    cli.add_command(contact_list)