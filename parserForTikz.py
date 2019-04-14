import sys
import re
import os
import copy
from pprint import pprint
from generateGraphml import Graph

def handleNode(G, line, globalProperties_2):
    NodeID = re.findall("\((\w+)\)", line)
    Location = re.findall("at[\s]*\((.*?)\)", line)
    NodeProperties = re.findall("\[(.*?)\]", line)
    Label = re.findall("{(.*)}", line)
    if NodeID:
        NodeID = NodeID[0]
    else:
        NodeID = None
    if Label and len(Label[0]) > 0:
        Label = Label[0]
    else:
        Label = None
    if(Location):
        coordinates = []
        for coord in Location[0].split(','):
            coordinates.append(coord)
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
        NodeProperties = {}
    # print "-------------------------------------NODESTART"
    # print line
    # TODO: NodeProperties may override some globalProperties

    if(globalProperties_2.has_key("node")):
        for k,v in globalProperties_2["node"].items():
            if k not in NodeProperties:
                NodeProperties[k] = v

    # print("NodeID : ", NodeID, "Label: ", Label, "Location: ", Location, "NodeProperties: ", NodeProperties)
    G.addNode(NodeID, Location[0], Location[1], label=Label, **NodeProperties)
    # print "-------------------------------------NODEEND"



# TODO : Handle Polar Coordinates
def handleDraw(line):
    print "TODO: ", line
    # pass
    # a = re.findall("\\\\draw[\s]*\((.*?)\)(.*?)\((.*?)\)", line)
    # if(a):
    #     A = a[0][0].split(",")
    #     B = a[0][1].strip()
    #     if(B== "ellipse"):
    #         C = a[0][2].split("and")
    #         C = [x.strip().strip("cm") for x in C]
    #     else:
    #         C = a[0][2].split(",")
    #     print A, B, C
    # else:
    #     print "todo : ", line
    #     a = re.findall("\\\\draw[\s]*\((.*?)\)(.*?)\((.*?)\)", line)
        
    
def parseTiKZ(inputFile):
    fileRegex = re.compile("(\s*\\[[^\\\\]*\\])((.|\n)*)", re.MULTILINE)
    z = fileRegex.match(inputFile)
    globalSpecs=z.groups()[0].strip()
    if(globalSpecs):
        globalSpecs = globalSpecs.strip("[").strip("]")
    brakets = 0
    joinedProp = []
    globalProperties = []
    for l in globalSpecs.split(','):
        if(brakets  > 0):
            brakets += l.count("{")-l.count("}")
            joinedProp.append(l)
            if(brakets==0):
                globalProperties.append(",".join(joinedProp))
        else:
            brakets += l.count("{")-l.count("}")
            if(brakets>0):
                joinedProp.append(l)
            else:
                globalProperties.append(l) 

    globalProperties_2 = {}
    for x in globalProperties:
        key, val =  x.split('=', 1)
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

                globalProperties_2["node"] = temp
        elif(key.__contains__("edge")):
            globalProperties_2["edge"] = val
        else:
            globalProperties_2[key] = val

    mainCode=z.groups()[1].strip()
    insideForEach=False
    maybeInsideForEach=False
    block = []
    G = Graph()
    for line in mainCode.split(';'):
        line=line.strip()
        if(line.__contains__("\\draw")):
            handleDraw(line)
        if(line.__contains__("\\node")):
            handleNode(G, line, globalProperties_2)

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
        print ("======================================")
        print ("Parsing File :", fileName)
        print (fileContent)
        print ("======================================")
        try:
            graphml = parseTiKZ(fileContent.strip()).encode("utf-8")
            with open( fileName_prefix + "t" + str(j) + graphml_suffix, 'w') as outFile:
                outFile.write(graphml)
        except Warning as e:
            print("WARN -> File {} :: RUNTIME ERROR :: {}".format(fileName, e))

        j+=1
    
