import api_client
import click
import printer
from click.decorators import option

contactlists_route = "/api/v2/outbound/contactlists"

@click.group()
def contactlists():
    """Functions to handle Contact Lists"""
    pass

@contactlists.command()
def list():
    """Listing Contact Lists"""
    client = api_client.ApiClient()
    response = client.get(contactlists_route)
    printer.print_name_id_data(response['entities'])

@contactlists.command()
@click.argument("contactlist_id")
def get(contactlist_id):
    """List specific Contact List"""
    client = api_client.ApiClient()
    response = client.get(contactlists_route+"/{}".format(contactlist_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(contactlists)