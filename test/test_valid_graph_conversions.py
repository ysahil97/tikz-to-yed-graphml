import os
import unittest
from parseTikz import ParseTikz

x = [
    {
        "inputFilePath": "./TestCases/valid-graphs/tex/example_test.tex",
        "expectedOutputPathPrefix": "./TestCases/valid-graphs/graphml/example_test.tex_",
        "numTikzTestCases": 1
    },
    {
        "inputFilePath": "./TestCases/valid-graphs/tex/edge-editing-v2.tex",
        "expectedOutputPathPrefix": "./TestCases/valid-graphs/graphml/edge-editing-v2.tex_",
        "numTikzTestCases": 8
    },
    {
        "inputFilePath": "./TestCases/valid-graphs/tex/rg-v2.tex",
        "expectedOutputPathPrefix": "./TestCases/valid-graphs/graphml/rg-v2.tex_",
        "numTikzTestCases": 3
    }
]


class TestValidGraphConversions(unittest.TestCase):
    def test_split(self):
        scale = 200
        logLevel = 0
        prefix = "test"
        directory = os.path.join(os.getcwd(), "output")

        TikzConverter = ParseTikz()
        graphmlCounter = 0
        for i in x:
            inputFilePath = os.path.join(os.getcwd(), i["inputFilePath"])
            generated_str = ""
            expected_str = ""

            TikzConverter.run(scale, logLevel, inputFilePath, prefix, directory)

            for j in range(i["numTikzTestCases"]):

                expectedOutputPath = os.path.join(os.getcwd(), i["expectedOutputPathPrefix"] + str(j) + "_graph.graphml")
                generatedOutputPath = os.path.join(directory, prefix + "_" + str(graphmlCounter) + "_graph.graphml")

                with open(expectedOutputPath, 'r') as f:
                    expected_str = f.read()

                with open(generatedOutputPath, 'r') as f:
                    generated_str = f.read()

                self.assertMultiLineEqual(expected_str, generated_str)
                graphmlCounter += 1


if __name__ == '__main__':
    unittest.main()
