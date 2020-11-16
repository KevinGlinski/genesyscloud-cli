import api_client
import click
from click.decorators import option

campaign_route = "/api/v2/outbound/campaigns"

@click.group()
def campaign():
    """Functions to handle Campaigns"""
    pass

@campaign.command()
def list():
    """Listing Campaigns"""
    client = api_client.ApiClient()
    return client.get(campaign_route)

@campaign.command()
@option("--campaign_id", "-c", required=True, type=str)
def get(campaign_id):
    """List specific Campaigns"""
    client = api_client.ApiClient()
    return client.get(campaign_route+"/{}".format(campaign_id))


def register(cli):
    cli.add_command(campaign)