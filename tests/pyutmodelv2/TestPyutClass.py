
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutClass import PyutClass
from pyutmodelv2.PyutLinkedObject import PyutLinkedObject
from pyutmodelv2.enumerations.PyutDisplayParameters import PyutDisplayParameters
from pyutmodelv2.enumerations.PyutStereotype import PyutStereotype
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

    def testLinksAndParent(self):

        pyutClass: PyutClass = PyutClass(name='CheckLinks')
        self.assertTrue(len(pyutClass.parents) == 0, 'No parents at instantiation')
        self.assertTrue(len(pyutClass.links) == 0, 'No links at instantiation')

    def testBasicProperties(self):
        pyutClass: PyutClass = PyutClass(name='CheckAttributes')

        self.assertEqual(PyutDisplayParameters.UNSPECIFIED, pyutClass.displayParameters)
        self.assertEqual(PyutStereotype.NO_STEREOTYPE, pyutClass.stereotype)
        self.assertEqual(True, pyutClass.displayStereoType)

    def testPyutObjectProperties(self):

        fakeClass: PyutClass = PyutClass(name='FakeClass')

        self.assertEqual('FakeClass', fakeClass.name, '')
        pyutClass: PyutClass = PyutClass(name='CheckPyutObject')

        self.assertTrue(pyutClass.id != 0)
        self.assertTrue(pyutClass.fileName == '')

    def testLinkedObject(self):

        pyutLinkedObject: PyutLinkedObject = PyutLinkedObject()

        self.assertTrue(len(pyutLinkedObject.parents) == 0, 'No parents at instantiation')
        self.assertTrue(len(pyutLinkedObject.links) == 0, 'No links at instantiation')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutClass))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
