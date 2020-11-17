import campaign
import chat_command
import click
import contact_list
import division
import group
import location
import notifications_command
import presence
import profile_command
import queue
import skill
import user


@click.group()
@click.option('--output', default="", help='Output format for commands (json, yaml, table)')
@click.option('--profile', default="", help='Which configured profile to use')
def cli(output, profile):
    """The Genesys Cloud cli is a tool to interact with Genesys Cloud"""
    click.get_current_context().meta['output'] = output
    click.get_current_context().meta['profile'] = profile
    

campaign.register(cli)
profile_command.register(cli)
chat_command.register(cli)
notifications_command.register(cli)
contact_list.register(cli)
division.register(cli)
group.register(cli)
location.register(cli)
presence.register(cli)
# queue.register(cli)
skill.register(cli)
user.register(cli)
