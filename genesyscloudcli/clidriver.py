import campaigns
import chat_command
import click
import contact_lists
import divisions
import groups
import locations
import notifications_command
import presences
import profile_command
import queues
import skills
import users


@click.group()
@click.option('--output', default="", help='Output format for commands (json, yaml, table)')
@click.option('--profile', default="", help='Which configured profile to use')
def cli(output, profile):
    """The Genesys Cloud cli is a tool to interact with Genesys Cloud"""
    click.get_current_context().meta['output'] = output
    click.get_current_context().meta['profile'] = profile
    

campaigns.register(cli)
profile_command.register(cli)
chat_command.register(cli)
notifications_command.register(cli)
contact_lists.register(cli)
divisions.register(cli)
groups.register(cli)
locations.register(cli)
presences.register(cli)
queues.register(cli)
skills.register(cli)
users.register(cli)
