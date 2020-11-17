import api_client
import click
import printer
from click.decorators import option

division_route = "/api/v2/authorization/divisions"

@click.group()
def divisions():
    """Functions to handle Divisions"""
    pass

@divisions.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Divisions"""
    client = api_client.ApiClient()
    response = client.get(division_route)
    
    if full:
        printer.print_json(response['entities'])
    else:
        printer.print_name_id_data(response['entities'])

@divisions.command()
@click.argument("division_id")
def get(division_id):
    """List a specific division"""
    client = api_client.ApiClient()
    response = client.get(division_route+"/{}".format(division_id))
    printer.print_json(response)

def register(cli):
    cli.add_command(divisions)