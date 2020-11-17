import api_client
import click
from click.decorators import option

presence_route = "/api/v2/presencedefinitions"

@click.group()
def presences():
    """Functions to handle Divisions"""
    pass

@presences.command()
def list():
    """Listing Presence Definitions"""
    client = api_client.ApiClient()
    return client.get(presence_route)

@presences.command()
@click.argument("presence_id")
def get(presence_id):
    """List specific Presence Definition"""
    client = api_client.ApiClient()
    return client.get(presence_route+"/{}".format(presence_id))


def register(cli):
    cli.add_command(presences)