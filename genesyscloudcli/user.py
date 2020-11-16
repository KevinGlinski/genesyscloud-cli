import api_client
import click
from click.decorators import option

user_route = "/api/v2/users"

@click.group()
def user():
    """Functions to handle Users"""
    pass

@user.command()
def list():
    """Listing Users"""
    client = api_client.ApiClient()
    return client.get(user_route)

@user.command()
@option("--userId", "-u", required=True, type=str)
def list(user):
    """Get specific Users"""
    client = api_client.ApiClient()
    return client.get(user_route+"/{}".format(user))


def register(cli):
    cli.add_command(user)