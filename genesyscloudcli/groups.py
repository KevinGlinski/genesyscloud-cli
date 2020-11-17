import api_client
import click
import printer
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
    response = client.get(group_route)
    printer.print_name_id_data(response['entities'])

@groups.command()
@click.argument("group_id")
def get(group_id):
    """List a specific Group"""
    client = api_client.ApiClient()
    response = client.get(group_route+"/{}".format(group_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(groups)