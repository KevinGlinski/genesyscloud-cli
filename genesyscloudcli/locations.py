import api_client
import click
import printer
from click.decorators import option

locations_route = "/api/v2/locations"

@click.group()
def locations():
    """Functions to handle locations"""
    pass

@locations.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing locations"""
    client = api_client.ApiClient()
    response = client.get(locations_route)
    
    if full:
        printer.print_json(response['entities'])
    else:
        printer.print_name_id_data(response['entities'])

@locations.command()
@click.argument("location_id")
def get(location_id):
    """List specific locations"""
    client = api_client.ApiClient()
    response = client.get(locations_route+"/{}".format(location_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(locations)