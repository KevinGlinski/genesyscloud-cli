import click

@click.group()
def chat():
    """Functions to create chat interactions"""
    pass

@chat.command()
def deployments():
    """Gets a list of chat deployments"""
    mgr = profile_handler.ProfileHandler()
    mgr.new_profile()


@profile.command()
@click.argument('chatdeployment')
@click.argument('queuename')
@click.option('--chatdeployment', default="", help='Name of chat deployment to use, if not specified uses the first one found')
def new():
    """Creates a new chat"""
    mgr = profile_handler.ProfileHandler()
    mgr.new_profile()
