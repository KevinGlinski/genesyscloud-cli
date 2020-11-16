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
def cli():
    """Entry point"""
    pass


campaign.register(cli)
profile_command.register(cli)
chat_command.register(cli)
notifications_command.register(cli)
contact_list.register(cli)
division.register(cli)
group.register(cli)
location.register(cli)
presence.register(cli)
queue.register(cli)
skill.register(cli)
user.register(cli)
