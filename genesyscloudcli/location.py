import api_client
import click
from click.decorators import option

locations_route = "/api/v2/locations"

@click.group()
def locations():
    """Functions to handle locations"""
    pass

@locations.command()
def list():
    """Listing locations"""
    client = api_client.ApiClient()
    return client.get(locations_route)

@locations.command()
@option("--location_id", "-l", required=True, type=str)
def get(locations_id):
    """List specific locations"""
    client = api_client.ApiClient()
    return client.get(locations_route+"/{}".format(locations_id))


def register(cli):
    cli.add_command(locations)