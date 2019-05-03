import os
import unittest
from tikz2graphml.parseTikz import ParseTikz

"""
Driver stub to iterate over all the possible test cases for automatic testing
"""
x = [
    {
        "inputFilePath": "./TestCases/invalid-graphs/tex/SyntaxError_1.tex",
    },
    {
        "inputFilePath": "./TestCases/invalid-graphs/tex/NodeMissingFromEdge_1.tex",
    },
    {
        "inputFilePath": "./TestCases/invalid-graphs/tex/NotSupportedDrawShapes_1.tex",
    },
    {
        "inputFilePath": "./TestCases/invalid-graphs/tex/NotSupportedGlobalProperties_1.tex",
    }
]

"""
Module to automate testing of valid graph test cases
"""
class TestInValidGraphConversions(unittest.TestCase):
    def test_split(self):
        scale = 100
        prefix = "test"
        directory = os.path.join(os.getcwd(), "output")
        TikzConverter = ParseTikz()

        for i in x:
            inputFilePath = os.path.join(os.getcwd(), i["inputFilePath"])
            try:
                TikzConverter.run(float(scale), inputFilePath, prefix, directory)
                # If run completed successfully, that means code is not failing => something wrong
                print("ERROR :::: No Exception was thrown. This should not have happened")
                assert False
            except Exception as e:
                print("Exception Raised :: {}. A good Thing.".format(e))
                assert True

if __name__ == '__main__':
    unittest.main()
