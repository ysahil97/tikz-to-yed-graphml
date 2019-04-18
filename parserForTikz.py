import sys
import re
import os
import copy
from pprint import pprint
from generateGraphml import Graph



def handleNode(G, line, globalProperties):
    #  \node (nodeidentifier) at (Location: polar or cartession) {Label};
     # This regex will capture the alphanumeric text inside parenthesis since Location involves ',' and ':' which are not alphanumeric, it won't be captures 
    NodeID = re.findall("\((\w+)\)", line)
    # Location is always in parenthesis after at .. so search for "at ()" and capture the text inside parenthesis
    Location = re.findall("at[\s]*\((.*?)\)", line)
    # everything inside [] is nodeproperties
    NodeProperties = re.findall("\[(.*?)\]", line)
    # Text inside {} contains node label
    Label = re.findall("{(.*)}", line)
    if NodeID:
        NodeID = NodeID[0]
    else:
        NodeID = None
    if Label and len(Label[0]) > 0:
        Label = Label[0]
    else:
        Label = None
    
    if Location:
        coordinates = []
        for coord in Location[0].split(','):
            coordinates.append(coord)
        Location = coordinates
    else:
        Location = None
    
    if NodeProperties:
        properties = {}
        for prop in NodeProperties[0].split(','):
            l = prop.split('=')
            properties[l[0]] = l[1]
        NodeProperties = properties
    else:
        NodeProperties = {}
    # print("-------------------------------------NODESTART")
    # print(line)
    # TODO: NodeProperties may override some globalProperties
    if globalProperties and "scale" in globalProperties:
        if "scale" not in NodeProperties:
            NodeProperties["scale"] = globalProperties["scale"]

    if globalProperties and "node" in globalProperties:
        for k,v in globalProperties["node"].items():
            if k not in NodeProperties:
                NodeProperties[k] = v
    
    # print("NodeID : ", NodeID, "Label: ", Label, "Location: ", Location, "NodeProperties: ", NodeProperties)
    G.addNode(NodeID, Location[0], Location[1], label=Label, **NodeProperties)
    # if(globalProperties and globalProperties.has_key("node")):
    #     globalNodeProp = globalProperties["node"]
    # else:
    #     for key, val in NodeProperties.iteritems():
    #         print key, val

    # if(NodeProperties):
    #     for key, val in globalNodeProp.iteritems():
    #         if(NodeProperties.has_key(key)):
    #             print key, NodeProperties[key]
    #         else:
    #             print key, val
    # else:
    #     for key, val in globalNodeProp.iteritems():
    #         print key, val



# TODO : Handle Polar Coordinates
def handleDraw(G, line):
    # This regex helps to know if it is draw of type
    # \draw [properties]? node1 -- node2 -- node3 -- ..... 
    regexToMatchOnlyDrawLine = re.compile("\\\\draw.*?(\\-\\-\s*\(.*?\))+", re.MULTILINE)
    if(regexToMatchOnlyDrawLine.match(line.strip())):
        # get them as group
        matchGroup = re.findall("\\\\draw\s*(\[(.*?)\])?(.*)", line)
        if (matchGroup):
            allNodes = matchGroup[0][2]
            props = matchGroup[0][1]
        nodes = [x.strip().strip(")").strip("(") for x in allNodes.split("--")]
        for i in range(len(nodes)-1):
            print("line from ", nodes[i], " to ", nodes[i+1])
            G.addEdge(nodes[i], nodes[i+1])
        print("PROPS", props, allNodes)
        return

    #  To match \draw properties? node1 edge node2
    # Example
    # \draw[->] (n2) edge (n0);
    # NOT DONE: \draw[->] (n2) edge[bend right = 45] (n0);
    regexToMatchOnlyEdge = re.compile("\\\\draw\s*(\[.*?\])?\s*(\(.*?\)\s*edge\s*\(.*?\))", re.MULTILINE)
    matched=regexToMatchOnlyEdge.match(line)
    if(matched):
        allNodes = matched.group(2)
        props = matched.group(1)
        nodes = [x.strip().strip(")").strip("(") for x in allNodes.split("edge")]
        for i in range(len(nodes)-1):
            print("Edge from ", nodes[i], " to ", nodes[i+1])
            G.addEdge(nodes[i], nodes[i+1])
        print("Edge PROPS", props, allNodes)
        return

    # #  To match \draw properties? node1 rectangle node2
    # # Example
    # # \draw (n1) rectangle (n2);
    regexToMatchOnlyRectangle = re.compile("\\\\draw\s*(\(.*?\)\s*rectangle\s*\(.*?\))", re.MULTILINE)
    # may need if rect prop in [] are there
    # regexToMatchOnlyRectangle = re.compile("\\\\draw\s*(\[.*?\])?\s*(\(.*?\)\s*rectangle\s*\(.*?\))", re.MULTILINE)
    matched=regexToMatchOnlyRectangle.match(line)
    if(matched):
        coordinates = matched.group(1)
        nodes = [x.strip().strip(")").strip("(") for x in coordinates.split("rectangle")]
        print(nodes)
        for i in range(len(nodes)-1):
            coordinates_XY = [x.strip() for x in nodes[i].split(',')]
            coordinates_X1Y1 = [x.strip() for x in nodes[i+1].split(',')]

            x, y = float(coordinates_XY[0]), float(coordinates_XY[1])
            x1, y1 = float(coordinates_X1Y1[0]), float(coordinates_X1Y1[1])
            length = x - x1
            width = y - y1
            print("rectangle at (", x, ") .... (", y + width, ")", "length : ", length, "  , width : ", width)
            G.addShape(None, x, y + width, abs(length*10), abs(width*10), shape="rectangle")
        return

    #  To match \draw properties? node1 rectangle node2
    # Example
    # \draw (n1) ellipse (n2);
    # regexToMatchOnlyellipse_may_NEED_IF_PROP_clause_there = re.compile("\\\\draw\s*(\[.*?\])?\s*(\(.*?\)\s*ellipse\s*\(.*?\))", re.MULTILINE)
    regexToMatchOnlyellipse = re.compile("\\\\draw\s*(\(.*?\)\s*ellipse\s*\(.*?\))", re.MULTILINE)
    matched=regexToMatchOnlyellipse.match(line)
    if(matched):
        coordinates = matched.group(1)
        nodes = [x.strip().strip(")").strip("(") for x in coordinates.split("ellipse")]
        for i in range(len(nodes)-1):
            print("ellipse at (", nodes[i], ") .... (", nodes[i+1], ")")
        return

    # To match \draw Location node[NodeProp] {Label}
    # Example
    # \draw (0*360/5: 3.5cm) node[fill=green!90]{};
    regexToMatchDrawNode = re.compile("\\\\draw\s*(\((.*?)\).*?node.*?\[(.*?)\]\s*{(.*?)})", re.MULTILINE)
    matched=regexToMatchDrawNode.match(line)
    if(matched):
        Location = matched.group(2)
        Props = matched.group(3)
        Label = matched.group(4)
        print("Draw Node ", Label, " at ", Location, "with Props (", Props, ")")
        return
    print("TODO: ", line, "Exiting")
    sys.exit(1)



    #     A = a[0][0].split(",")
    #     B = a[0][1].strip()
    #     if(B== "ellipse"):
    #         C = a[0][2].split("and")
    #         C = [x.strip().strip("cm") for x in C]
    #     else:
    #         C = a[0][2].split(",")
    #     print(A, B, C)
    # else:
    #     print("todo : ", line)
    #     a = re.findall("\\\\draw[\s]*\((.*?)\)(.*?)\((.*?)\)", line)
        

# Get globalSpecs and Code from inputFile
# Go through mainCode and handle each instruction (Only node for now)
def parseTiKZ(inputFile):
    # Tikz Code format is :
    # [GlobalProperties] MainCode
    # This regex captures GlobalProperties and MainCode as group 0 and 1 respectively
    fileRegex = re.compile("(\s*\\[[^\\\\]*\\])((.|\n)*)", re.MULTILINE)
    z = fileRegex.match(inputFile)
    if(len(z.groups())!=3):
        print ("Cannot Parse file")
        return
    matchedGlobalSpecs=z.groups()[0]
    if(matchedGlobalSpecs):
        matchedGlobalSpecs = matchedGlobalSpecs.strip().strip("[").strip("]")
    brakets = 0
    subProp = []
    allProps = []
    # Normal split won't work in cases like below
    # scale=.8,auto=center,every node/.style={circle,inner sep=4pt}
    # Because of "every node/.style={circle,inner sep=4pt}"
    for l in matchedGlobalSpecs.split(','):
        if(brakets  > 0):
            brakets += l.count("{")-l.count("}")
            subProp.append(l)
            if(brakets==0):
                allProps.append(",".join(subProp))
        else:
            brakets += l.count("{")-l.count("}")
            if(brakets>0):
                subProp.append(l)
            else:
                allProps.append(l) 

    globalProperties = {}
    for prop in allProps:
        key, val =  prop.split('=', 1)
        if(key.__contains__("node")):
            val = val.strip("{").strip("}")
            temp = {}
            for r in val.split(","):
                temp_2 = r.split("=")
                if(len(temp_2) >= 2):
                    k, v = temp_2[0], temp_2[1]
                    k = k.replace(" ", "_")
                    temp[k] = v
                else:
                    temp["shape"] = temp_2[0]

                globalProperties["node"] = temp
        elif(key.__contains__("edge")):
            # TODO: Not seen this so not handled (added just in case)
            globalProperties["edge"] = val
        else:
            globalProperties[key] = val

    tikzCode=z.groups()[1].strip()
    G = Graph()
    for line in tikzCode.split(';'):
        line=line.strip()
        if(line.__contains__("\\draw")):
            handleDraw(G, line)
        if(line.__contains__("\\node")):
            handleNode(G, line, globalProperties)

    return G.get_graph()


if __name__ == "__main__":
    # fileName = "TestCases/rg-v2.tex"
    fileName_prefix="./edge-editing-v2.tex"
    fileName_suffix="_unrolled.tex"
    graphml_suffix = ".graphml"
    j=0
    while(os.path.exists(fileName_prefix + "t" + str(j) + fileName_suffix)):
        fileName = fileName_prefix + "t" + str(j) + fileName_suffix
        with open(fileName) as inputFile:
            fileContent = inputFile.read()
        print("======================================")
        print("Parsing File :", fileName)
        # print(fileContent)
        print("======================================")
        try:
            graphml = parseTiKZ(fileContent.strip()).encode("utf-8")
            with open( fileName_prefix + "t" + str(j) + graphml_suffix, 'wb') as outFile:
                outFile.write(graphml)
        except Warning as e:
            print("WARN -> File {} :: WARNING :: {}".format(fileName, e))
        j+=1
