import pyperclip
import typer
from cryptography.fernet import InvalidToken

from commands.config import get_encryption_phrase, verify_master_password
from crypto import decrypt
from storage import load_vault


def reveal(site: str):
    """Copy password to clipboard."""
    vault = load_vault()

    if not vault:
        typer.echo("No entries found.")
        return

    entry = vault.get(site)
    if entry is None:
        typer.echo("Site not found.")
        return

    try:
        if not verify_master_password():
            typer.echo("Incorrect master password.")
            raise typer.Exit(code=1)

        encryption_phrase = get_encryption_phrase()
    except ValueError as error:
        typer.echo(str(error))
        raise typer.Exit(code=1)

    try:
        password = decrypt(entry["password"], encryption_phrase)
    except InvalidToken:
        typer.echo("Unable to decrypt password. Check encryption phrase.")
        raise typer.Exit(code=1)

    pyperclip.copy(password)
    typer.echo("Password copied to clipboard.")
