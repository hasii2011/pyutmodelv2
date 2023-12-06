
from typing import List


from unittest import TestSuite

from unittest import main as unitTestMain

from copy import deepcopy

from pyutmodelv2.PyutField import PyutField
from pyutmodelv2.PyutType import PyutType

from pyutmodelv2.enumerations.PyutVisibility import PyutVisibility

from tests.ProjectTestBase import ProjectTestBase


class TestPyutField(ProjectTestBase):

    fieldNames:        List[str]      = ['field1', 'field2', 'field3']
    fieldTypes:        List[PyutType] = [PyutType(value='int'),
                                         PyutType(value='bool'),
                                         PyutType(value='float')]
    fieldValues:       List[str]      = ['22', 'False', '62.34324']
    fieldVisibilities: List[PyutVisibility] = [PyutVisibility.PRIVATE,
                                               PyutVisibility.PUBLIC,
                                               PyutVisibility.PROTECTED
                                               ]

    def setUp(self):
        super().setUp()

    def testDeepCopyList(self):

        originalFields: List[PyutField] = []
        for x in range(len(TestPyutField.fieldNames)):
            field: PyutField = PyutField(name=TestPyutField.fieldNames[x],
                                         fieldType=TestPyutField.fieldTypes[x],
                                         defaultValue=TestPyutField.fieldValues[x],
                                         visibility=TestPyutField.fieldVisibilities[x]
                                         )
            originalFields.append(field)
        self.logger.info(f'originalFields: {originalFields}')

        dopplegangers: List[PyutField] = deepcopy(originalFields)
        self.logger.info(f'{dopplegangers=}')

        for pyutField in dopplegangers:
            self.assertTrue(isinstance(pyutField.type, PyutType), 'Wrong type copied')
            self.assertTrue(isinstance(pyutField.visibility, PyutVisibility), 'Wrong visibility type copied')

    def testBasicStringRepresentation(self):

        basicField: PyutField = PyutField(name='basicField',
                                          fieldType=PyutType('int'),
                                          defaultValue='42',
                                          visibility=PyutVisibility.PUBLIC)

        expectedValue: str = '+basicField: int = 42'
        actualValue:   str = basicField.__str__()

        self.assertEqual(expectedValue, actualValue, 'Basic string representation broken')

    def testNoDefaultValueStringRepresentation(self):

        noDefaultValueField: PyutField = PyutField(name='basicField',
                                                   fieldType=PyutType('int'),
                                                   visibility=PyutVisibility.PRIVATE)

        expectedValue: str = '-basicField: int'
        actualValue:   str = noDefaultValueField.__str__()

        self.assertEqual(expectedValue, actualValue, 'Basic string representation broken')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutField))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
