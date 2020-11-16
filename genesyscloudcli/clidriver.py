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
def cli():
    """Entry p"""
    pass


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
