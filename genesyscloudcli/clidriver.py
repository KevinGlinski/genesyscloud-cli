import click
import profile_command
import chat_command
import notifications_command

@click.group()
def cli():
    pass



profile_command.register(cli)
chat_command.register(cli)
notifications_command.register(cli)