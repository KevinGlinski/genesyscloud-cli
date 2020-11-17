import api_client
import click
import printer
from click.decorators import option

campaigns_route = "/api/v2/outbound/campaigns"

@click.group()
def campaigns():
    """Functions to handle Campaigns"""
    pass

@campaigns.command()
def list():
    """List Campaigns"""
    client = api_client.ApiClient()
    response = client.get(campaigns_route)
    printer.print_name_id_data(response['entities'])

@campaigns.command()
@click.argument("campaign_id")
def get(campaign_id):
    """List a specific Campaign"""
    print(campaign_id)
    client = api_client.ApiClient()
    response = client.get(campaigns_route+"/{}".format(campaign_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(campaigns)