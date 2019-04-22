import sys
import antlr4
import logging
from grammar.TikzLexer import TikzLexer
from grammar.TikzParser import TikzParser
from grammar.TikzListener import TikzListener
from CustomTikzListener import CustomTikzListener

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-1s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main():
    inputFileName = './TestCases/graph.tex'
    input_stream = antlr4.FileStream(inputFileName)
    lexer = TikzLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = TikzParser(stream)
    tree = parser.begin()

    htmlChat = CustomTikzListener(inputFileName, './TestCases/graph.graphml')
    walker = antlr4.ParseTreeWalker()
    walker.walk(htmlChat, tree)


if __name__ == '__main__':
    main()

