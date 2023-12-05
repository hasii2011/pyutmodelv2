
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutObject import PyutObject
from pyutmodelv2.PyutObject import infiniteSequence

from tests.TestBase import TestBase


class TestPyutObject(TestBase):
    """
    """
    def setUp(self):

        super().setUp()
        PyutObject.idGenerator = infiniteSequence()

    def tearDown(self):
        pass

    def testNoName(self):
        pyutObject: PyutObject = PyutObject()

        expectedSize: int = 0
        actualSize:   int = pyutObject.name.__len__()

        self.assertEqual(expectedSize, actualSize, 'Name should be empty')

    def testNoNameValue(self):

        pyutObject: PyutObject = PyutObject()

        actualName:     str = pyutObject.name

        self.assertIsNotNone(actualName, 'Should have some value')

        expectedLength: int = 0
        actualLength:   int = len(actualName)

        self.assertEqual(expectedLength, actualLength, 'Should be empty')

    def testProvidedName(self):

        providedName: str = 'El Gato Malo'
        nameLength:   int = len(providedName)

        pyutObject: PyutObject = PyutObject(providedName)

        expectedLength: int = nameLength
        actualLength:   int = len(pyutObject.name)

        self.assertEqual(expectedLength, actualLength, 'Our name appears to have NOT been used')


    def testHowIdsIncrement(self):

        pyutObject1: PyutObject = PyutObject(name='pyutObject1')
        self.assertEqual(0, pyutObject1.id, f'{pyutObject1.name} - Incorrect id')

        pyutObject2: PyutObject = PyutObject(name='pyutObject2')
        self.assertEqual(1, pyutObject2.id, f'{pyutObject2.name} - Incorrect id')

        pyutObject3: PyutObject = PyutObject(name='pyutObject3')
        self.assertEqual(2, pyutObject3.id, f'{pyutObject3.name} - Incorrect id')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutObject))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
