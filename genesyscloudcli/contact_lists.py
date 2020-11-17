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
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Contact Lists"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(contactlists_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@contactlists.command()
@click.argument("contactlist_id")
def get(contactlist_id):
    """List specific Contact List"""
    client = api_client.ApiClient()
    response = client.get(contactlists_route+"/{}".format(contactlist_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(contactlists)