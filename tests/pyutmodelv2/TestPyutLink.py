
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutLink import PyutLink
from pyutmodelv2.PyutSDInstance import PyutSDInstance
from pyutmodelv2.PyutSDMessage import PyutSDMessage
from pyutmodelv2.enumerations.PyutLinkType import PyutLinkType

from tests.ProjectTestBase import ProjectTestBase


class TestPyutLink(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()
        # import warnings
        # To ignore this warning:
        # DeprecationWarning
        # Since this is legacy stuff;  May go away
        # warnings.simplefilter("ignore", category=DeprecationWarning)

    def tearDown(self):
        pass

    def testValidLinkType(self):

        pyutLink: PyutLink = PyutLink(name='ValidPyutLink')
        linkType: PyutLinkType = PyutLinkType.COMPOSITION

        pyutLink.linkType = linkType

        expectedLinkType: PyutLinkType = PyutLinkType.COMPOSITION
        actualLinkType:   PyutLinkType = pyutLink.linkType

        self.assertEqual(expectedLinkType, actualLinkType, 'Incorrect  valid legacy type support')

    def testLinkAssignment(self):

        sourceInstance:      PyutSDInstance = PyutSDInstance(instanceName='SourceInstance')
        destinationInstance: PyutSDInstance = PyutSDInstance(instanceName='DestinationInstance')

        message: PyutSDMessage = PyutSDMessage(message='callback')
        message.source      = sourceInstance
        message.destination = destinationInstance

        checkSource: PyutSDInstance = message.source
        self.assertIsNotNone(checkSource, 'Did we pass')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutLink))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
