import sys
import antlr4
import logging
import os
from grammar.TikzLexer import TikzLexer
from grammar.TikzParser import TikzParser
from grammar.TikzListener import TikzListener
from CustomTikzListener import CustomTikzListener
from extradeCodeInsideTikzAndUnrollForeach import getCodeInsideTIKZAfterUnrolling

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-1s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main():
    directory="./TestCases"
    filename="graph.tex"

    for value in getCodeInsideTIKZAfterUnrolling(directory, filename):  
        print("===================================")
        print (value)
        print("===================================")
        input_stream = antlr4.InputStream(value)
        lexer = TikzLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = TikzParser(stream)
        tree = parser.begin()

        j = 0
        while(os.path.exists(filename + "t" + str(j) + "_unrolled.tex")):
            j+=1
        saveTo = directory +"/" + filename + "_" + str(j) + "_graph.graphml"
        htmlChat = CustomTikzListener(filename, saveTo)
        walker = antlr4.ParseTreeWalker()
        walker.walk(htmlChat, tree)

if __name__ == '__main__':
    main()

