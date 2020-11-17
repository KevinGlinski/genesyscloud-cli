import api_client
import click
import printer
from click.decorators import option

users_route = "/api/v2/users"

@click.group()
def users():
    """Functions to handle Users"""
    pass

@users.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Users"""
    client = api_client.ApiClient()
    response = client.get(users_route)

    if full:
        printer.print_json(response['entities'])
    else:
        printer.print_name_id_data(response['entities'])

@users.command()
@click.argument("user_id")
def get(user_id):
    """Get a specific User"""
    client = api_client.ApiClient()
    response = client.get(users_route+"/{}".format(user_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(users)