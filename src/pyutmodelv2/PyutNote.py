from logging import Logger
from logging import getLogger

from pyutmodelv2.PyutLinkedObject import PyutLinkedObject


class PyutNote(PyutLinkedObject):
    def __init__(self):
        self.logger: Logger = getLogger(__name__)
