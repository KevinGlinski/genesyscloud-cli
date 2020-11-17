import api_client
import click
import printer
from click.decorators import option

presence_route = "/api/v2/presencedefinitions"

@click.group()
def presence():
    """Functions to handle Divisions"""
    pass

@presence.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Presence Definitions"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(presence_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)
    

@presence.command()
@click.argument("presence_id")
def get(presence_id):
    """List specific Presence Definition"""
    client = api_client.ApiClient()
    response = client.get(presence_route+"/{}".format(presence_id))
    printer.print_json(response)

def register(cli):
    cli.add_command(presence)