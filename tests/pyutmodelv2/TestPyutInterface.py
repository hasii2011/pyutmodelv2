
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutInterface import PyutInterface

from tests.ProjectTestBase import ProjectTestBase


class TestPyutInterface(ProjectTestBase):
    """
    You need to change the name of this class to Test`xxxx`
    Where `xxxx` is the name of the class that you want to test.

    See existing tests for more information.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testInstantiation(self):

        pyutInterface: PyutInterface = PyutInterface(name='OzzeeInterface')

        self.assertIsNotNone(pyutInterface.implementors, 'Ensure we can access this property')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutInterface))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
