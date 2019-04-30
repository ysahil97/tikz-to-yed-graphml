import unittest
from parseTikz import ParseTikz

x = [
    {
        "inputFilePath" : "./TestCases/label.tex",
        "generatedOutputPath" : "./TestCases/label.tex_0_graph.graphml",
        "expectedOutputPath" : "./TestCases/label.tex_legacy_0_graph.graphml"
    }
]

class TestValidGraphConversions(unittest.TestCase):
    def __init__(self):
        self.parseModule = ParseTikz()
        self.directory = "./TestCases"
        self.scale = 200

    def test_split(self):
        Tikz_parse = ParseTikz()
        # Tikz_parse.run(scalingFactor, logLevel, inputFileName, prefix, directory)
        for i in x:
            inputFilePath = i["inputFilePath"]
            generated_str = ""
            expected_str = ""
            with open(i["expectedOutputPath"],'r') as f:
                expected_str = f.read().replace('\n', '')
            self.parseModule.run(self.scale,self.scale,inputFilePath,inputFilePath,self.directory)
            with open(i["generatedOutputPath"],'r') as f:
                generated_str = f.read().replace('\n', '')
            assertMultiLineEqual(expected_str,generated_str)
        # s = 'hello world'
        # self.assertEqual(s.split(), ['hello', 'world'])
        # with self.assertRaises(TypeError):
        #     s.split(2)

if __name__ == '__main__':
    unittest.main()
