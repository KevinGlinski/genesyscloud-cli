import api_client
import click
from click.decorators import option

group_route = "/api/v2/groups"

@click.group()
def groups():
    """Functions to handle Groups"""
    pass

@groups.command()
def list():
    """Listing Groups"""
    client = api_client.ApiClient()
    return client.get(group_route)

@groups.command()
@click.argument("group_id")
def get(group_id):
    """List a specific Group"""
    client = api_client.ApiClient()
    return client.get(group_route+"/{}".format(group_id))


def register(cli):
    cli.add_command(groups)