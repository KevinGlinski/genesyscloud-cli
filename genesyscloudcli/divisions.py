import api_client
import click
from click.decorators import option

division_route = "/api/v2/authorization/divisions"

@click.group()
def divisions():
    """Functions to handle Divisions"""
    pass

@divisions.command()
def list():
    """List Divisions"""
    client = api_client.ApiClient()
    return client.get(division_route)

@divisions.command()
@click.argument("division_id")
def get(division_id):
    """List a specific division"""
    client = api_client.ApiClient()
    return client.get(division_route+"/{}".format(division_id))


def register(cli):
    cli.add_command(divisions)