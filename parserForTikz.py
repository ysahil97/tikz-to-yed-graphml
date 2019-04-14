import sys
import re
import os
import copy
from pprint import pprint

def handleNode(line):
    NodeID = re.findall("\((\w+)\)", line)
    Location = re.findall("at[\s]*\((.*?)\)", line)
    NodeProperties = re.findall("\[.*?\]", line)
    Label = re.findall("{.*}", line)
    if NodeID:
        NodeID = NodeID[0]
    else:
        NodeID = None
    if(Label):
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
        NodeProperties = None
    # print "-------------------------------------NODESTART"
    # print line
    print NodeID, 
    print Label,
    print Location, 
    print NodeProperties
    # print "-------------------------------------NODEEND"



def handleDraw(line):
    # print "TODO: ", line
    pass
    # TODO : Handle Polar Coordinates
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
    #     print "TODO : ", line
    #     a = re.findall("\\\\draw[\s]*\((.*?)\)(.*?)\((.*?)\)", line)
        
    


def handleForeach(block):
    # print block
    # sys.exit(1)

    line = block[0]
    if(len(block) > 1 and block[1].strip()=="{"):
        remainBlock='\n'.join(block[2:])
    else:
        remainBlock='\n'.join(block[1:])
                
    # print remainBlock, block
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
            toReturn.append(copy.copy(newBlock).strip())
    # print toReturn
    # sys.exit(1)
    for line in toReturn:
        # print "----------->" , line
        if(line.__contains__("\\node")):
           handleNode(line)
        if(line.__contains__("\\draw")):
            handleDraw(line)








def parseTiKZ(inputFile):
    print "INPUT FILE STARTS --------------------------------"
    print inputFile
    print "INPUT FILE ENDS --------------------------------"
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
                    temp[k] = v
                else:
                    temp["shape"] = temp_2[0]

                globalProperties_2["node"] = temp
        elif(key.__contains__("edge")):
            globalProperties_2["edge"] = val
        else:
            globalProperties_2[key] = val
    print globalProperties_2
    mainCode=z.groups()[1].strip()
    insideForEach=False
    maybeInsideForEach=False
    block = []
    for line in mainCode.split(';'):
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
            # print "-------->", line
            brackets = brackets + line.count("{") - line.count("}")                
            # if(line[0] == "{"):
            if(brackets==0):
                insideForEach=False
                handleForeach(block)
                # print "CASE_A_:", block
                block = []
            # else:
                
            #     insideForEach=False
            #     handleForeach(block)
            #     # print "CASE_B_:", block
            #     block = []
            # continue
                
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

if __name__ == "__main__":
    # fileName = "TestCases/rg-v2.tex"
    fileName="TestCases/edge-editing-v2.tex"
    with open(fileName) as inputFile:
        fileContent = inputFile.read()
    regextToGetTikzPictureCode = re.compile("\\\\end[\s]*{tikzpicture}", re.MULTILINE)

    tikzBlocks = []
    for x in regextToGetTikzPictureCode.split(fileContent):
        if(x.__contains__("tikzpicture")):
            tikzBlocks.append(x)
    count = -1
    for x in tikzBlocks:
        for y in (re.split("\\\\begin{tikzpicture}", x)):
            count += 1
            if(count%2==1):
                parseTiKZ(y)
                # sys.exit(1)
