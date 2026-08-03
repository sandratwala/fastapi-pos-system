import hashlib
import os


def hash_password(plain_password: str) -> str:
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + plain_password).encode()).hexdigest()
    return f"{salt}${hashed}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    salt, hashed = hashed_password.split("$")
    return hashlib.sha256((salt + plain_password).encode()).hexdigest() == hashed