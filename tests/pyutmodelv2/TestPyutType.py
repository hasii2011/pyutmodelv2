
from typing import List

from unittest import main as unitTestMain
from unittest import TestSuite

from copy import deepcopy

from pyutmodelv2.PyutType import PyutType

from tests.ProjectTestBase import ProjectTestBase


class TestPyutType(ProjectTestBase):

    def setUp(self):
        super().setUp()

    def testDeepCopyPyutTypes(self):

        typeValues:    List[str]      = ['int', 'bool', 'float']
        originalTypes: List[PyutType] = []

        for aValue in typeValues:
            pyutType: PyutType = PyutType(value=aValue)
            originalTypes.append(pyutType)
        self.logger.info(f'{originalTypes=}')

        # noinspection SpellCheckingInspection
        doppleGangers: List[PyutType] = deepcopy(originalTypes)

        # noinspection SpellCheckingInspection
        self.logger.info(f'{doppleGangers=}')

        self.assertIn(member=originalTypes[0], container=doppleGangers, msg='')
        self.assertIn(member=originalTypes[1], container=doppleGangers, msg='')
        self.assertIn(member=originalTypes[2], container=doppleGangers, msg='')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutType))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
