import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


# ⚠️ For now static salt (we’ll improve later)
SALT = b"pmcli_static_salt"


def derive_key(master_password: str) -> bytes:
    """Derive encryption key from master password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))


def encrypt(text: str, master_password: str) -> str:
    key = derive_key(master_password)
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()


def decrypt(token: str, master_password: str) -> str:
    key = derive_key(master_password)
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()