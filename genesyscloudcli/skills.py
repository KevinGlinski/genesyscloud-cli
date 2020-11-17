import api_client
import click
import printer
from click.decorators import option

skills_route = "/api/v2/routing/skills"

@click.group()
def skills():
    """Functions to handle skills"""
    pass

@skills.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List skills"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(skills_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@skills.command()
@click.argument("skill_id")
def get(skill_id):
    """List a specific skill"""
    client = api_client.ApiClient()
    response = client.get(skills_route+"/{}".format(skill_id))
    printer.print_json(response)


def register(cli):
    cli.add_command(skills)