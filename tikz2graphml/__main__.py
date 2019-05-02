import argparse
from tikz2graphml.parseTikz import ParseTikz

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-h", "--help", type=int, help="Print this menu")
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity", default=0)
    parser.add_argument("-s", "--scale", default=200, type=float, help="Scaling Factor")
    parser.add_argument("-i", "--input", type=str, help="Input file path", required=True)
    parser.add_argument("-p", "--prefix", type=str, help="Output file Prefix")
    parser.add_argument("-d", "--directory", default="./output", type=str, help="Output file directory")

    args = parser.parse_args()

    scalingFactor = args.scale
    logLevel = args.verbosity
    inputFileName = args.input
    prefix = args.prefix
    directory = args.directory

    ParseTikz().run(scalingFactor, logLevel, inputFileName, prefix, directory)


if __name__ == '__main__':
    main()
