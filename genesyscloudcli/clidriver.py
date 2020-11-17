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
import search
import skills
import users


@click.group()
@click.option('--output', default="", help='Output format for commands (json, yaml, table)')
@click.option('--profile', default="", help='Which configured profile to use')
@click.option('--page-size', default=250, help='Set a page size other')
@click.option('--page', default=-1, help='Return a specific page')
def cli(output, profile, page_size, page):
    """The Genesys Cloud cli is a tool to interact with Genesys Cloud"""
    click.get_current_context().meta['output'] = output
    click.get_current_context().meta['profile'] = profile
    click.get_current_context().meta['page_size'] = page_size
    click.get_current_context().meta['page'] = page    
    

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
search.register(cli)
users.register(cli)
