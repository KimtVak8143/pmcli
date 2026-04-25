import getpass

import typer

from commands.config import get_encryption_phrase
from crypto import encrypt
from storage import load_vault, save_vault


def add(site: str):
    """Add a new credential."""
    vault = load_vault()

    if site in vault:
        overwrite = typer.confirm("Entry already exists. Overwrite?")
        if not overwrite:
            typer.echo("Cancelled.")
            return

    username = input("Username: ").strip()
    if not username:
        typer.echo("Username cannot be empty.")
        raise typer.Exit(code=1)

    password = getpass.getpass("Password: ")
    if not password.strip():
        typer.echo("Password cannot be empty.")
        raise typer.Exit(code=1)

    try:
        encryption_phrase = get_encryption_phrase()
    except ValueError as error:
        typer.echo(str(error))
        raise typer.Exit(code=1)

    encrypted_password = encrypt(password, encryption_phrase)

    vault[site] = {
        "username": username,
        "password": encrypted_password,
    }

    save_vault(vault)
    typer.echo("Credential saved securely.")
