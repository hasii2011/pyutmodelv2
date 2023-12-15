
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutClass import PyutClass
from pyutmodelv2.PyutLinkedObject import PyutLinkedObject

from pyutmodelv2.PyutObject import PyutObject
from pyutmodelv2.PyutObject import infiniteSequence

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

    def testBasicPropertiesDisplayParameters(self):

        pyutClass: PyutClass = PyutClass(name='CheckDisplayProperties')
        self.assertEqual(PyutDisplayParameters.UNSPECIFIED, pyutClass.displayParameters)

    def testBasicPropertiesStereotype(self):

        pyutClass: PyutClass = PyutClass(name='CheckStereotype')
        self.assertEqual(PyutStereotype.NO_STEREOTYPE, pyutClass.stereotype)

    def testBasicPropertiesDisplayStereotype(self):

        pyutClass: PyutClass = PyutClass(name='CheckDisplayStereotype')
        self.assertEqual(True, pyutClass.displayStereoType)

    def testBasicPropertiesInterfaces(self):

        pyutClass: PyutClass = PyutClass(name='CheckInterfaces')
        self.assertTrue(len(pyutClass.interfaces) == 0, 'Where is my top level attribute`')

    def testIdIncrements(self):

        PyutObject.idGenerator = infiniteSequence()
        fakeClass: PyutClass = PyutClass(name='FakeClass')

        self.assertEqual('FakeClass', fakeClass.name, '')
        pyutClass: PyutClass = PyutClass(name='CheckPyutObject')

        self.assertTrue(pyutClass.id == 1)
        self.assertTrue(pyutClass.fileName == '')

        pyutClass = PyutClass(name='BumpId')
        self.assertTrue(pyutClass.id == 2)

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
