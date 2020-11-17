import api_client
import click
from click.decorators import option

campaign_route = "/api/v2/outbound/campaigns"

@click.group()
def campaigns():
    """Functions to handle Campaigns"""
    pass

@campaigns.command()
def list():
    """List Campaigns"""
    client = api_client.ApiClient()
    return client.get(campaign_route)

@campaigns.command()
@click.argument("campaign_id")
def get(campaign_id):
    """List a specific Campaign"""
    print(campaign_id)
    client = api_client.ApiClient()
    return client.get(campaign_route+"/{}".format(campaign_id))


def register(cli):
    cli.add_command(campaigns)