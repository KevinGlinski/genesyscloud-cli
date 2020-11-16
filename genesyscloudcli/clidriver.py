import click
import profile_command

@click.group()
def cli():
    pass


profile_command.register(cli)