import typer

from storage import load_vault


def list_sites():
    """List stored sites."""
    vault = load_vault()

    if not vault:
        typer.echo("No entries found.")
        return

    for site in sorted(vault.keys()):
        typer.echo(site)
