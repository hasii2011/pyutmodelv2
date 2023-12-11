
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutParameter import PyutParameter
from pyutmodelv2.PyutType import PyutType

from tests.ProjectTestBase import ProjectTestBase


class TestPyutParameter(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testFullString(self):
        pyutParameter: PyutParameter = PyutParameter(name='Ozzee', parameterType=PyutType('float'), defaultValue='1.0')

        expectedValue: str = 'Ozzee: float = 1.0'
        actualValue:   str = pyutParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'Full string representation has changed')

    def testIndividualAttributes(self):
        pyutParameter: PyutParameter = PyutParameter(name='Ozzee', parameterType=PyutType('float'), defaultValue='1.0')

        self.assertEqual('Ozzee', pyutParameter.name, 'Parameter name not correct')
        self.assertEqual('1.0', pyutParameter.defaultValue, 'default value not set correctly')
        self.assertEqual(PyutType('float'), pyutParameter.type, 'Type not set correctly')

    def testNoDefaultValue(self):
        pyutParameter: PyutParameter = PyutParameter(name='Ozzee', parameterType=PyutType('float'))

        expectedValue: str = 'Ozzee: float'
        actualValue:   str = pyutParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'No default value string representation has changed')

    def testNoTypeOrDefaultValue(self):

        pyutParameter: PyutParameter = PyutParameter(name='Ozzee')

        expectedValue: str = 'Ozzee'
        actualValue:   str = pyutParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'No Type, no default value string representation has changed')

    def testDataClassRepr(self):

        pyutParameter: PyutParameter = PyutParameter(name='Ozzee', parameterType=PyutType('float'), defaultValue='1.0')

        expectedValue: str = 'Ozzee: float = 1.0'
        actualValue:   str = pyutParameter.__repr__()

        self.assertEqual(expectedValue, actualValue, 'Full string representation has changed')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutParameter))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
