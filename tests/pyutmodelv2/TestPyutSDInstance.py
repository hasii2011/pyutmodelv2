
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutSDInstance import PyutSDInstance

from tests.ProjectTestBase import ProjectTestBase


class TestPyutSDInstance(ProjectTestBase):
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

    def testProperties(self):

        pyutSDInstance: PyutSDInstance = PyutSDInstance()

        self.assertTrue(pyutSDInstance.name == '', '')

        self.assertTrue(pyutSDInstance.fileName == '')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutSDInstance))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
