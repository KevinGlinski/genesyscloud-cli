import api_client
import click
from click.decorators import option

division_route = "/api/v2/authorization/divisions"

@click.group()
def division():
    """Functions to handle Divisions"""
    pass

@division.command()
def list():
    """Listing Divisions"""
    client = api_client.ApiClient()
    return client.get(division_route)

@division.command()
@option("--division_id", "-d", required=True, type=str)
def get(division_id):
    """List specific division"""
    client = api_client.ApiClient()
    return client.get(division_route+"/{}".format(division_id))


def register(cli):
    cli.add_command(division)