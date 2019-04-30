import unittest
from parseTikz import ParseTikz

x = [
    {
        "inputFilePath" : "./TestCases/label.tex",
        "expectedOutputPath" : "./TestCases/label.tex_0_graph.graphml"
        "generatedOutputPath" : "./TestCases/label.tex_legacy_0_graph.graphml"
    }
]

class TestValidGraphConversions(unittest.TestCase):
    def __init__():
        self.parseModule = ParseTikz()

    def test_split(self):
        for i in x:
            inputFilePath = i["inputFilePath"]
            
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
