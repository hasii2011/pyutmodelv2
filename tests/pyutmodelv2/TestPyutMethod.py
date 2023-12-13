

from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodelv2.PyutMethod import PyutMethod
from pyutmodelv2.PyutMethod import PyutParameters
from pyutmodelv2.PyutMethod import SourceCode
from pyutmodelv2.PyutParameter import PyutParameter
from pyutmodelv2.PyutType import PyutType

from tests.ProjectTestBase import ProjectTestBase


class TestPyutMethod(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()
        self._pyutMethod: PyutMethod = PyutMethod(name='methodName')

    def tearDown(self):
        pass

    def testUpdateEmptyParameters(self):

        pyutMethod:    PyutMethod    = PyutMethod(name='MethodToBuildUp')
        pyutParameter: PyutParameter = PyutParameter(name='InitialParameter')

        pyutMethod.addParameter(parameter=pyutParameter)

        self.assertEqual(1, len(pyutMethod.parameters), "There can be only one")

    def testStringMethodWithParametersRepresentation(self):

        pyutMethod: PyutMethod = self._pyutMethod
        pyutMethod.returnType = PyutType('float')

        pyutMethod.parameters = self._makeParameters()

        defaultName:            str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(intParam: int = 0, floatParam: float = 32.0): float'
        actualRepresentation:   str = pyutMethod.methodWithParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testStringMethodWithoutParametersRepresentation(self):

        pyutMethod:     PyutMethod = self._pyutMethod
        pyutMethod.returnType = PyutType('float')

        pyutMethod.parameters = self._makeParameters()

        defaultName:            str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(): float'
        actualRepresentation:   str = pyutMethod.methodWithoutParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testMethodSimpleParametersWithParameters(self):
        simpleMethod: PyutMethod = self._pyutMethod

        simpleMethod.parameters = self._makeSimpleParameters()

        defaultName: str = 'methodName'
        expectedRepresentation: str = (
            f'+{defaultName}('
            f'{simpleMethod.parameters[0].name}, '
            f'{simpleMethod.parameters[1].name}, '
            f'{simpleMethod.parameters[2].name}'
            ')'
        )
        actualRepresentation:   str = simpleMethod.methodWithParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Simple Method Simple Parameters does not match')

    def testStashSourceCode(self):

        pyutMethod:        PyutMethod = self._generateAMethod()
        expectedLineCount: int = 5
        actualLineCount:   int = len(pyutMethod.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def testChangeSourceCode(self):
        pyutMethod:        PyutMethod = self._generateAMethod()
        #
        # This is NOT the recommended way to update the source code
        #
        pyutMethod.sourceCode.insert(2, '# I am a comment')
        expectedLineCount: int = 6
        actualLineCount:   int = len(pyutMethod.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def _generateAMethod(self) -> PyutMethod:
        pyutMethod: PyutMethod    = PyutMethod(name='OzzeeElGatoDiablo')

        pyutMethod.sourceCode = SourceCode(
            [
                'weLeft:           bool = True',
                'isOzzeeAGoodGato: bool = False',
                'if weLeft is True:',
                '    isOzzeeAGoodGato = True',
                'return isOzzeeAGoodGato'
            ]
        )
        return pyutMethod

    def _makeParameters(self) -> PyutParameters:

        pyutParameter1: PyutParameter  = PyutParameter(name='intParam', type=PyutType("int"), defaultValue='0')
        pyutParameter2: PyutParameter  = PyutParameter(name='floatParam', type=PyutType("float"), defaultValue='32.0')
        parameters:     PyutParameters = PyutParameters([pyutParameter1, pyutParameter2])

        return parameters

    def _makeSimpleParameters(self) -> PyutParameters:
        """
        No types, no default values
        """
        intParameter:   PyutParameter  = PyutParameter(name='intParameter')
        floatParameter: PyutParameter  = PyutParameter(name='floatParameter')
        boolParameter:  PyutParameter  = PyutParameter(name='boolParameter')

        parameters:     PyutParameters = PyutParameters([intParameter, floatParameter, boolParameter])

        return parameters


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutMethod))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
