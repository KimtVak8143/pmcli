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

## Commands

Show help:

```bash
pmenv/bin/python main.py --help
```

Add a credential:

```bash
pmenv/bin/python main.py add github.com
```

List saved sites:

```bash
pmenv/bin/python main.py list
```

Get the username for a site:

```bash
pmenv/bin/python main.py get github.com
```

Copy the password for a site to your clipboard:

```bash
pmenv/bin/python main.py reveal github.com
```

`reveal` asks for your master password. It does not print the saved password.

## Fresh Start

To clear all saved data:

```bash
echo "{}" > ~/.pmcli/vault.json
```
