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
@click.argument("location_id")
def get(location_id):
    """List specific locations"""
    client = api_client.ApiClient()
    return client.get(locations_route+"/{}".format(location_id))


def register(cli):
    cli.add_command(locations)