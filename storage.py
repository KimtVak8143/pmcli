import json
from pathlib import Path

VAULT_DIR = Path.home() / ".pmcli"
VAULT_FILE = VAULT_DIR / "vault.json"


def init_storage():
    """Ensure storage exists"""
    VAULT_DIR.mkdir(exist_ok=True)

    if not VAULT_FILE.exists():
        with open(VAULT_FILE, "w") as f:
            json.dump({}, f)


def load_vault():
    """Load vault data"""
    init_storage()

    with open(VAULT_FILE, "r") as f:
        return json.load(f)


def save_vault(data: dict):
    """Save vault data"""
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=4)