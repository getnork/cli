from nork.commands import nork, typer
import os


@nork.command(name="os:cwd")
def handle():
    """
    Get the current working directory
    """
    typer.echo(os.getcwd())
