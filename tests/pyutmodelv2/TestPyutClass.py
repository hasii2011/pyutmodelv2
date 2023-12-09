
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutClass import PyutClass
from tests.ProjectTestBase import ProjectTestBase

# import the class you want to test here
# from org.pyut.template import template


class TestPyutClass(ProjectTestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testMultipleInheritance(self):

        pyutClass: PyutClass = PyutClass(name='')
        self.logger.info(f'{len(pyutClass.fields)=}')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutClass))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
