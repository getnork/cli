import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    NOR/K CLI
    """


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
