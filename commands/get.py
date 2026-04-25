import typer

from storage import load_vault


def get(site: str):
    """Get username."""
    vault = load_vault()

    if not vault:
        typer.echo("No entries found.")
        return

    entry = vault.get(site)
    if entry is None:
        typer.echo("Site not found.")
        return

    typer.echo(entry["username"])
