import sys
import antlr4
import logging
import os
from grammar.TikzLexer import TikzLexer
from grammar.TikzParser import TikzParser
from grammar.TikzListener import TikzListener
from CustomTikzListener import CustomTikzListener
from extradeCodeInsideTikzAndUnrollForeach import getCodeInsideTIKZAfterUnrolling
import argparse

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-1s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main():
    directory="./TestCases"
    filename="graph.tex"
    # filename="edge-editing-v2.tex"

    for value in getCodeInsideTIKZAfterUnrolling(directory, filename):  
        logger.info("===================================")
        logger.info("\n\n" + value + "\n\n")
        logger.info("===================================")
        input_stream = antlr4.InputStream(value)
        lexer = TikzLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = TikzParser(stream)
        tree = parser.begin()

        # we save file as filename_t_{n}_graph.graphml
        j = 0
        while(os.path.exists(directory +"/" + filename + "_" + str(j) + "_graph.graphml")):
            j+=1
        outputFilename = directory +"/" + filename + "_" + str(j) + "_graph.graphml"
        htmlChat = CustomTikzListener(filename, outputFilename)
        walker = antlr4.ParseTreeWalker()
        walker.walk(htmlChat, tree)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("-h", "--help", type=int, help="Print this menu")
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
    parser.add_argument("-s", "--scale", type=float, help="Scaling Factor")
    parser.add_argument("-prefix",type=str, help="Output file Prefix")
    
    args = parser.parse_args()
    
    scalingFactor = args.scale
    logLevel = args.scale
    prefix = args.prefix

    main()

