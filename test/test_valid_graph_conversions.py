import unittest 

x = [
    {
        "inputFilePath" : "./TestCases/valid1.tex",
        "expectedOutputPath" : 
        "generatedOutputPath" : 
    }
] 

class TestValidGraphConversions(unittest.TestCase): 

    def test_split(self):         
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2) 
  
if __name__ == '__main__': 
    unittest.main() 
