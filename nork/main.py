import typer
from . import __version__

app = typer.Typer(help=f"NOR/K {typer.style(__version__, fg=typer.colors.GREEN)}")

@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
