import api_client
import click
from click.decorators import option

skill_route = "/api/v2/routing/skills"

@click.group()
def skill():
    """Functions to handle skills"""
    pass

@skill.command()
def list():
    """Listing skills"""
    client = api_client.ApiClient()
    return client.get(skill_route)

@skill.command()
@option("--skill_id", "-s", required=True, type=str)
def get(skill_id):
    """List specific skill"""
    client = api_client.ApiClient()
    return client.get(skill_route+"/{}".format(skill_id))


def register(cli):
    cli.add_command(skill)