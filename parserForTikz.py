import sys
import re
import os
import copy
from pprint import pprint



def handleNode(line, globalProperties):
    #  \node (nodeidentifier) at (Location: polar or cartession) {Label};
     # This regex will capture the alphanumeric text inside parenthesis since Location involves ',' and ':' which are not alphanumeric, it won't be captures 
    NodeID = re.findall("\((\w+)\)", line)
    # Location is always in parenthesis after at .. so search for "at ()" and capture the text inside parenthesis
    Location = re.findall("at[\s]*\((.*?)\)", line)
    # everything inside [] is nodeproperties
    NodeProperties = re.findall("\[.*?\]", line)
    # Text inside {} contains node label
    Label = re.findall("{.*}", line)

    if NodeID:
        NodeID = NodeID[0]
    else:
        NodeID = None

    if Label:
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
        NodeProperties = None

    # print "-------------------------------------NODESTART"
    # print line
    print NodeID,
    print Label,
    print Location,
    globalNodeProp = {}

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

    print(NodeProperties, globalProperties)
    
    # print "-------------------------------------NODEEND"



# TODO : Handle Polar Coordinates
# TODO : Handle all draw cases
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
    for prop in globalProperties:
        key, val =  prop.split('=', 1)
        if(key.__contains__("node")):
            val = val.strip("{").strip("}")
            temp = {}
            for r in val.split(","):
                temp_2 = r.split("=")
                if(len(temp_2) >= 2):
                    k, v = temp_2[0], temp_2[1]
                    temp[k] = v
                else:
                    temp["shape"] = temp_2[0]

                globalProperties["node"] = temp
        elif(key.__contains__("edge")):
            # TODO: Not seen this so not handled (added just in case)
            globalProperties["edge"] = val
        else:
            globalProperties[key] = val

    print globalProperties

    tikzCode=z.groups()[1].strip()
    for line in tikzCode.split(';'):
        line=line.strip()
        if(line.__contains__("\\draw")):
            handleDraw(line)
        if(line.__contains__("\\node")):
            handleNode(line, globalProperties)

if __name__ == "__main__":
    # fileName = "TestCases/rg-v2.tex"
    fileName_prefix="/home/pankaj/acads/Sem8/softEng/project/tikz-to-yed-graphml/edge-editing-v2.tex"
    fileName_suffix="_unrolled.tex"
    j=0
    while(os.path.exists(fileName_prefix + "t" + str(j) + fileName_suffix)):
        fileName = fileName_prefix + "t" + str(j) + fileName_suffix
        with open(fileName) as inputFile:
            fileContent = inputFile.read()
        print ("======================================")
        print ("Parsing File :", fileName)
        # print (fileContent)
        print ("======================================")
        parseTiKZ(fileContent.strip())
        j+=1
