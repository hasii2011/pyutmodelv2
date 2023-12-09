
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutUseCase import PyutUseCase

from tests.ProjectTestBase import ProjectTestBase


class TestPyutCase(ProjectTestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testInstantiation(self):
        pyutUseCase: PyutUseCase = PyutUseCase(name='Ozzee')

        self.assertIsNotNone(pyutUseCase, 'Wowza, I made it')

    def testInstantiationNoName(self):
        pyutUseCase: PyutUseCase = PyutUseCase()

        self.assertIsNotNone(pyutUseCase, 'Wowza, I made it')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutCase))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
