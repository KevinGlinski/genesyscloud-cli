import api_client
import click
from click.decorators import option

group_route = "/api/v2/groups"

@click.group()
def group():
    """Functions to handle Groups"""
    pass

@group.command()
def list():
    """Listing Groups"""
    client = api_client.ApiClient()
    return client.get(group_route)

@group.command()
@option("--group_id", "-g", required=True, type=str)
def get(group_id):
    """List specific Group"""
    client = api_client.ApiClient()
    return client.get(group_route+"/{}".format(group_id))


def register(cli):
    cli.add_command(group)