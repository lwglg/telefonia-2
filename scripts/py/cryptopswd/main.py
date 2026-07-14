import os, base64, hashlib

__all__ = ["generate_hash_salt_for_password"]


def generate_hash_salt_for_password(password: str, iterations: int, hash_name: str = "sha256", random_size: int = 16) -> tuple[str, str]:
    salt = os.urandom(random_size)
    dk = hashlib.pbkdf2_hmac(hash_name, password.encode("utf-8"), salt, iterations, dklen=64)

    return base64.b64encode(dk).decode(), base64.b64encode(salt).decode()
