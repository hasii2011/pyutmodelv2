
from logging import Logger
from logging import getLogger

from pyutmodelv2.PyutClassCommon import PyutClassCommon
from pyutmodelv2.PyutLinkedObject import PyutLinkedObject


class PyutClass(PyutClassCommon, PyutLinkedObject):

    def __init__(self, name: str):

        self.logger: Logger = getLogger(__name__)

        PyutLinkedObject.__init__(self, name)
        PyutClassCommon.__init__(self)
