from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

skills_route = "/api/v2/routing/skills"

@click.group()
def skills():
    """Functions to handle skills"""
    pass

@skills.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Skills"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(skills_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@skills.command()
@click.argument("skill_id")
def get(skill_id):
    """List a specific Skill"""
    client = api_client.ApiClient()
    response = client.get(skills_route+"/{}".format(skill_id))
    printer.print_data(response)


@skills.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new Skill"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(skills_route, data)
    printer.print_data(response)

def register(cli):
    cli.add_command(skills)