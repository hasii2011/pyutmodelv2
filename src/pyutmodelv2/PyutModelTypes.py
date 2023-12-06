
from typing import List
from typing import NewType

from pyutmodelv2.PyutField import PyutField

ClassName    = NewType('ClassName', str)
Implementors = NewType('Implementors', List[ClassName])

PyutFields   = NewType('PyutFields',  List[PyutField])
