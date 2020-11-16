import api_client
import click
from click.decorators import option

skills_route = "/api/v2/routing/skills"

@click.group()
def skills():
    """Functions to handle skills"""
    pass

@skills.command()
def list():
    """List skills"""
    client = api_client.ApiClient()
    return client.get(skills_route)

@skills.command()
@click.argument("skill_id")
def get(skill_id):
    """List a specific skill"""
    client = api_client.ApiClient()
    return client.get(skills_route+"/{}".format(skill_id))


def register(cli):
    cli.add_command(skills)