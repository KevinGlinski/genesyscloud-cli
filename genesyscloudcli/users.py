from yaml import error
import api_client
import click
import json
import printer
import sys
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
@click.argument('input', nargs=-1)
def new(input):
    """Create a new user"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.
    
    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = get_json(input)
    client = api_client.ApiClient()
    response = client.post(users_route, data)
    printer.print_json(response)


def get_json(input):
    if type(input) is tuple:
        input = input[0]
    try:
        return json.loads(input)
    except (ValueError, TypeError):
        if is_file(input):
            print("IS FILE")
            f = open(input, "r")
            return json.loads(f.read())
        elif is_json(input):
            print("IS JSON")
            return json.loads(json.dumps(input))
        else:
            raise ValueError("ERROR: Please input a valid JSON string or a file containing valid JSON")


def is_json(input):
    try:
        json.dumps(input)
        return True
    except (ValueError, TypeError):
        return False


def is_file(input):
    try:
        f = open(input, "r")
        return is_json(f.read())
    except (FileNotFoundError, TypeError):
        return False
        

def register(cli):
    cli.add_command(users)