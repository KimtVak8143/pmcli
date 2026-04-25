import typer

from commands.add import add
from commands.get import get
from commands.list_cmd import list_sites
from commands.reveal import reveal
from commands.start import start

app = typer.Typer(help="PMCLI - Your local password manager")

app.command()(add)
app.command()(get)
app.command(name="list")(list_sites)
app.command()(reveal)
app.command()(start)


if __name__ == "__main__":
    app()
