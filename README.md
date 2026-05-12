# PMCLI

A small local CLI password manager.

Passwords are encrypted and stored in:

```text
~/.pmcli/vault.json
```

## Setup

From the project folder:

```bash
cd pmcli
```

Create your local config:

```bash
cp .env.example .env
```

Edit `.env`:

```text
PMCLI_MASTER_PASSWORD=your-reveal-password
PMCLI_ENCRYPTION_PHRASE=your-stable-encryption-phrase
```

Important:

- `PMCLI_MASTER_PASSWORD` is used to allow `reveal`.
- `PMCLI_ENCRYPTION_PHRASE` is used to encrypt and decrypt saved passwords.
- Do not change `PMCLI_ENCRYPTION_PHRASE` after saving passwords, or old entries cannot be decrypted.

## Run From Anywhere On macOS/Linux

Create a small wrapper command:

```bash
mkdir -p ~/bin
nano ~/bin/pmcli
```

Paste this into the file:

```bash
#!/bin/bash
cd /Users/<Name>/Documents/ABCD/pmcli
exec pmenv/bin/python main.py "$@"
```

Make it executable:

```bash
chmod +x ~/bin/pmcli
```

Add `~/bin` to your shell path:

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Now you can run `pmcli` from anywhere:

```bash
pmcli --help
```

## Run From Anywhere On Windows

Create a folder for local commands:

```powershell
mkdir $HOME\bin
```

Create a file named:

```text
%USERPROFILE%\bin\pmcli.bat
```

Put this inside `pmcli.bat`:

```bat
@echo off
cd /d C:\path\to\ABCD\pmcli
pmenv\Scripts\python.exe main.py %*
```

Replace `C:\path\to\ABCD\pmcli` with the real path to your `pmcli` folder.

Add `bin` to your user PATH in PowerShell:

```powershell
[Environment]::SetEnvironmentVariable(
  "Path",
  $env:Path + ";$HOME\bin",
  "User"
)
```

Restart your terminal, then test:

```powershell
pmcli --help
```

## Commands

Show help:

```bash
pmcli --help
```

Add a credential:

```bash
pmcli add github.com
```

List saved sites:

```bash
pmcli list
```

Get the username for a site:

```bash
pmcli get github.com
```

Copy the password for a site to your clipboard:

```bash
pmcli reveal github.com
```

`reveal` asks for your master password. It does not print the saved password.

Without the wrapper, run commands from the `pmcli` folder like this:

```bash
pmenv/bin/python main.py list
```

## Fresh Start

To clear all saved data:

```bash
echo "{}" > ~/.pmcli/vault.json
```
