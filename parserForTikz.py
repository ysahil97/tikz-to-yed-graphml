import sys
import re
import os
import copy
from pprint import pprint

def handleNode(line):
    NodeID = re.findall("\((\w+)\)", line)
    Location = re.findall("at[\s]*\((.*?)\)", line)
    NodeProperties = re.findall("\[.*?\]", line)
    Label = re.findall("{.*?}", line)
    if NodeID:
        NodeID = NodeID[0]
    else:
        NodeID = None
    if(Label):
        Label = Label[0].strip('{').strip('}')
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
    # print "-------------------------------------NODESTART"
    # print line
    # print NodeID, 
    # print Label,
    # print Location, 
    # print NodeProperties
    # print "-------------------------------------NODEEND"



def handleDraw(line):
    a = re.findall("\\\\draw[\s]*\((.*?)\)(.*?)\((.*?)\)", line)
    A = a[0][0].split(",")
    B = a[0][1].strip()
    if(B== "ellipse"):
        C = a[0][2].split("and")
        C = [x.strip().strip("cm") for x in C]
    else:
        C = a[0][2].split(",")
    print A, B, C
    


def handleForeach(block):
    # print block

    line = block[0]
    remainBlock='\n'.join(block[1:])
    toReturn=[]
    if(line.__contains__("\\foreach")):
        searchIterators = re.findall("\\\\foreach(.*)in.*", line)
        if(searchIterators):
            searchIterators = searchIterators[0]
        
        loopIter = searchIterators.strip().split("/")
        variables = {}
        var_n_to_name = {}
        i = 0
        for var in loopIter:
            variables[var.strip("\\")] = None
            var_n_to_name[i] = var.strip("\\")

            i+=1
        
        domain = re.findall("{(.*)}", line)

        if(domain):
            domain = domain[0]
        # print(variables , domain)
        for a in domain.split(","):
            newBlock = copy.copy(remainBlock)
            for n, b in enumerate(a.split("/")):
                variables[var_n_to_name[n]] = b
                newBlock = re.sub("\\\\"+var_n_to_name[n], b, newBlock)
        
            toReturn.append(copy.copy(newBlock))
    # print "-------------------------------------FOREACH_START"
    # pprint (block)
    # pprint (toReturn)
    # print "-------------------------------------FOREACH_END"








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
    maybeInsideForEach=False
    block = []
    for line in mainCode.split('\n'):
        line=line.strip()
        brackets = 0
        if(line.__contains__("\\foreach")):
            x=re.findall("\\\\foreach.*in[\s]*{.*}(.*)", line)
            y=re.findall("\\\\foreach.*in[\s]*{.*?}.*", line)
            if(x):
                x = x[0]
            if(y):
                y = y[0]
            block.append(y)
            block.append(x)
            brackets = line.count("{") - line.count("}")
            insideForEach=True   

        elif(insideForEach):
            block.append(line)
            if(line[0] == "{"):
                brackets = brackets + line.count("{") - line.count("}")                
                if(brackets==0):
                    insideForEach=False
                    handleForeach(block)
                    # print "CASE_A_:", block
                    block = []
            else:
                insideForEach=False
                handleForeach(block)
                # print "CASE_B_:", block
                block = []
            continue
                
        if(line.__contains__("\\node")):
           handleNode(line)
        if(line.__contains__("\\draw")):
            handleDraw(line)


            

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
fileName="TestCases/edge-editing-v2.tex"
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
