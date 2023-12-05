
from dataclasses import dataclass


def infiniteSequence():
    num = 0
    while True:
        yield num
        num += 1


idGenerator = infiniteSequence()


@dataclass
class PyutObject:

    name:     str = ''
    id:       int = 0
    fileName: str = ''

    def __init__(self, name: str = ''):

        self.name = name
        self.id   = next(idGenerator)
