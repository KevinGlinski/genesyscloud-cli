
import profile_handler
import click

@click.group()
def profile():
    """Functions to manage credentials profiles"""
    pass

@profile.command()
def new():
    """Prompts user for new configuration section"""
    mgr = profile_handler.ProfileHandler()
    mgr.new_profile()

@profile.command()
@click.argument('profilename')
def setdefault(profilename):
    """Takes a profile by name and makes it the default configuration"""
    mgr = profile_handler.ProfileHandler()
    mgr.new_profile()


@profile.command()
def default():
    """Displays information on the current default configuration"""
    mgr = profile_handler.ProfileHandler()
    click.echo(mgr.get_profile(''))


def register(cli):
    cli.add_command(profile)