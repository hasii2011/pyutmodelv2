
from typing import ClassVar
from typing import Generator

from dataclasses import dataclass


def infiniteSequence() -> Generator[int, None, None]:
    num = 0
    while True:
        yield num
        num += 1


@dataclass
class PyutObject:
    idGenerator: ClassVar = infiniteSequence()

    name:     str = ''
    id:       int = 0
    fileName: str = ''

    def __init__(self, name: str = ''):

        self.name = name
        self.id   = next(PyutObject.idGenerator)
