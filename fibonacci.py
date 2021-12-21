"""
Implementação da sequência de Fibonacci utilizando gerador
"""

from typing import Generator


def fibonacci(
        number: int) -> Generator[int, None, None]:  # definindo unm gerador
    yield 0  # caso básico
    if number > 0: yield 1
    last: int = 0
    nxt: int = 1

    for _ in range(1, number):
        last, nxt = nxt, last + nxt
        yield nxt


if __name__ == '__main__':
    for i in fibonacci(14):
        print(i, end=' -> ')
    print('End')