import getpass
import os
from pathlib import Path


def get_encryption_phrase() -> str:
    phrase = _get_config_value("PMCLI_ENCRYPTION_PHRASE")
    if phrase:
        return phrase

    phrase = getpass.getpass("Encryption Phrase: ")
    if phrase:
        return phrase

    raise ValueError("Encryption phrase is required.")


def verify_master_password() -> bool:
    expected_master = _get_config_value("PMCLI_MASTER_PASSWORD")
    if not expected_master:
        raise ValueError("Master password is not configured.")

    entered_master = getpass.getpass("Master Password: ")
    return entered_master == expected_master


def _get_config_value(key: str) -> str | None:
    return os.environ.get(key) or _load_config_value_from_env_file(key)


def _load_config_value_from_env_file(key: str) -> str | None:
    for env_file in _env_file_paths():
        value = _read_config_value(env_file, key)
        if value:
            return value
    return None


def _env_file_paths() -> list[Path]:
    cwd_env = Path.cwd() / ".env"
    package_env = Path(__file__).resolve().parents[1] / ".env"
    return [cwd_env, package_env]


def _read_config_value(env_file: Path, expected_key: str) -> str | None:
    if not env_file.exists():
        return None

    with open(env_file, "r") as f:
        for line in f:
            key, separator, value = line.strip().partition("=")
            if separator and key == expected_key:
                return value.strip().strip("\"'")

    return None
