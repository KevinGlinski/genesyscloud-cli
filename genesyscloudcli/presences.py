import api_client
import click
from click.decorators import option

presence_route = "/api/v2/presencedefinitions"

@click.group()
def presence():
    """Functions to handle Divisions"""
    pass

@presence.command()
def list():
    """Listing Presence Definitions"""
    client = api_client.ApiClient()
    return client.get(presence_route)

@presence.command()
@option("--presence_id", "-p", required=True, type=str)
def get(presence_id):
    """List specific Presence Definition"""
    client = api_client.ApiClient()
    return client.get(presence_route+"/{}".format(presence_id))


def register(cli):
    cli.add_command(presence)