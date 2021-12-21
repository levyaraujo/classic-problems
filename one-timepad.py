from random import random
from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, 'big')


print(random_key(4))

# def decrypt(key1: int, key2: int) -> str:
