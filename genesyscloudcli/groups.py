from . import api_client
import click
from . import printer
from click.decorators import option

group_route = "/api/v2/groups"

@click.group()
def groups():
    """Functions to handle Groups"""
    pass

@groups.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Groups"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(group_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@groups.command()
@click.argument("group_id")
def get(group_id):
    """List a specific Group"""
    client = api_client.ApiClient()
    response = client.get(group_route+"/{}".format(group_id))
    printer.print_data(response)


def register(cli):
    cli.add_command(groups)