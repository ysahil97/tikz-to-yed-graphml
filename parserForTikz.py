import sys
import re
import os

def parseTiKZ(inputFile):
    """
    The file is of following syntax
        [scale=.8,auto=center,every node/.style={circle,inner sep=4pt}]
        \foreach \a in {0,1,2,...,10}{
            \draw (\a*360/20: 4cm) node[fill=blue!35]{};
        }
        \draw (10*360/20: 4cm) node[fill=blue!35]{1};
        \draw (9*360/20: 4cm) node[fill=blue!35]{2};
        \draw (1*360/20: 4cm) node[fill=blue!35]{\small{n-1}};
        \draw (0*360/20: 4cm) node[fill=blue!35]{$n$};
        \draw (7*360/20: 4cm) node[fill=black!15]{i};
        \draw (4*360/20: 4cm) node[fill=black!15]{j};
        \draw (7*360/20: 4cm) --(4*360/20: 4cm);
    """
    fileRegex = re.compile("(\s*\\[[^\\\\]*\\])((.|\n)*)", re.MULTILINE)
    z = fileRegex.match(inputFile)
    globalSpecs=z.groups()[0].strip()
    mainCode=z.groups()[1].strip()
    insideForEach=False
    for line in mainCode.split('\n'):
        line=line.strip()
        if(line.__contains__("\\node")):
            NodeID = re.findall("\((\w+)\)", line)
            Location = re.findall("at[\s]*\((.*?)\)", line)
            NodeProperties = re.findall("\[.*?\]", line)
            Label = re.findall("{.*?}", line)
            if NodeID:
                NodeID = NodeID[0]
            else:
                NodeID = None
            if(Label):
                Label = Label[0].strip('{').strip('}').strip("$")
            else:
                Label = None
            if(Location):
                coordinates = []
                for coord in Location[0].split(','):
                    coordinates.append(float(coord))
                Location = coordinates
            else:
                Location = None
            if(NodeProperties):
                properties = {}
                for prop in NodeProperties[0].split(','):
                    l = prop.split('=')
                    properties[l[0]] = l[1]
                NodeProperties = properties
            else:
                NodeProperties = None

            print NodeID, 
            print Label,
            print Location, 
            print NodeProperties

        # if(insideForEach):


            

    #         pass
    #     else:
    #         if(line.__contains__("foreach")):
    #             insideForEach=True
    #     print (line.strip())
    # if(line.__contains__("\\foreach")):
    #     if(line.__contains__("{")):
    #         foreach_brackets_opened=True

        
    # elif(line.__contains__("\\draw"))
    # elif(line.__contains__("\\node"))
    # elif(line.__contains__("foreach"))
    # elif(line.__contains__("foreach"))
    # elif(line.__contains__("foreach"))

    # sys.exit(1)

    




# fileName = "rg-v2.tex"
fileName="edge-editing-v2.tex"
with open(fileName) as inputFile:
    fileContent = inputFile.read()
regextToGetTikzPictureCode = re.compile("\\\\end[\s]*{tikzpicture}", re.MULTILINE)

z = []
for x in regextToGetTikzPictureCode.split(fileContent):
    if(x.__contains__("tikzpicture")):
        z.append(x)
count = -1
for x in z:
    for y in (re.split("\\\\begin{tikzpicture}", x)):
        count += 1
        if(count%2==1):
            z = parseTiKZ(y)
