import typer


def start():
    """Show the PMCLI welcome screen."""
    typer.echo(
        r"""
╭──────────────────────────────────────────────────────────────╮
│ 01010000 01001101 01000011 01001100 01001001       PMCLI     │
╰──────────────────────────────────────────────────────────────╯

      ██████╗ ███╗   ███╗ ██████╗██╗     ██╗
      ██╔══██╗████╗ ████║██╔════╝██║    
      ██████╔╝██╔████╔██║██║     ██║     ██║
      ██╔═══╝ ██║╚██╔╝██║██║     ██║     ██║
      ██║     ██║ ╚═╝ ██║╚██████╗███████╗██║
      ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚══════╝╚═╝

┏━━━━━━━━━━━━━━━━━━━━━ LOCAL VAULT ONLINE ━━━━━━━━━━━━━━━━━━━━━┓
┃                                                              ┃
┃              .--------.                                      ┃
┃             /  .--.   /|       vault: ~/.pmcli/vault.json    ┃
┃            /  /___/  / |       mode : local-only             ┃
┃           /_________/  |       keys : phrase-derived Fernet  ┃
┃           |  .----. |  |                                      ┃
┃           | |  ##  ||  |       reveal copies to clipboard    ┃
┃           | |  ##  ||  |       passwords stay off-screen     ┃
┃           |  '----' | /                                       ┃
┃           '---------'                                        ┃
┃                                                              ┃
┃      101101 ───── encrypted at rest ───── 011010             ┃
┃                                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

╭─ command deck ───────────────────────────────────────────────╮
│  pmcli add <site>       seal a new credential                 │
│  pmcli list             scan saved sites                      │
│  pmcli get <site>       show username only                    │
│  pmcli reveal <site>    copy password to clipboard            │
╰──────────────────────────────────────────────────────────────╯

status: armed   signal: clean   leak policy: zero screen secrets
"""
    )
