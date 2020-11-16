import click
import printer
import api_client

@click.group()
def chat():
    """Functions to create chat interactions"""
    pass

@chat.command()
def deployments():
    """Gets a list of chat deployments"""
    client = api_client.ApiClient()
    # printer.print_yaml(client.get('/api/v2/organizations/me'))
    printer.print_name_id_data(client.get("/api/v2/widgets/deployments")['entities'])


@chat.command()
@click.argument('chatdeployment')
@click.argument('queuename')
@click.option('--chatdeployment', default="", help='Name of chat deployment to use, if not specified uses the first one found')
def new(queue_name, chat_deployment):
    """Creates a new chat"""
    client = api_client.ApiClient()

    deployments = client.get("/api/v2/widgets/deployments")['entities']

    # if 

    mgr = profile_handler.ProfileHandler()
    mgr.new_profile()



def register(cli):
    cli.add_command(chat)