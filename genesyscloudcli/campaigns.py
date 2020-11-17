from . import api_client
import click
from . import printer
from click.decorators import option

campaigns_route = "/api/v2/outbound/campaigns"

@click.group()
def campaigns():
    """Functions to handle Campaigns"""
    pass

@campaigns.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Campaigns"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(campaigns_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@campaigns.command()
@click.argument("campaign_id")
def get(campaign_id):
    """List a specific Campaign"""
    print(campaign_id)
    client = api_client.ApiClient()
    response = client.get(campaigns_route+"/{}".format(campaign_id))
    printer.print_data(response)


def register(cli):
    cli.add_command(campaigns)