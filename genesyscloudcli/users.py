import api_client
import click
from click.decorators import option

users_route = "/api/v2/users"

@click.group()
def users():
    """Functions to handle Users"""
    pass

@users.command()
def list():
    """List Users"""
    client = api_client.ApiClient()
    return client.get(users_route)

@users.command()
@click.argument("user_id")
def list(user_id):
    """Get a specific User"""
    client = api_client.ApiClient()
    return client.get(users_route+"/{}".format(user_id))


def register(cli):
    cli.add_command(users)