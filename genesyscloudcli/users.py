from yaml import error
from . import api_client
import click
import json
from . import printer
from click.decorators import option

users_route = "/api/v2/users"

@click.group()
def users():
    """Functions to handle Users"""
    pass


@users.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Users"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(users_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)


@users.command()
@click.argument('user_id')
def get(user_id):
    """Get a specific User"""
    client = api_client.ApiClient()
    response = client.get(users_route+"/{}".format(user_id))
    printer.print_data(response)


@users.command()
@click.argument('input')
def new(input):
    """Create a new user"""
    if is_json(input):
        client = api_client.ApiClient()
        response = client.post(users_route, json.loads(input))
        printer.print_json(response)
    elif is_file(input):
        #it's a file so do file things
        client = api_client.ApiClient()
        f = open(input, "r")
        text = f.read()
        response = client.post(users_route, json.loads(text))
        printer.print_json(response)
    else:
        print("ERROR: Please input a valid JSON string or a file containing valid JSON")


def is_json(input):
    try:
        json.loads(input)
    except ValueError as e:
        return False
    
    return True

def is_file(input):
    try:
        f = open(input, "r")
        return is_json(f.read())
    except FileNotFoundError as e:
        return False
        

def register(cli):
    cli.add_command(users)