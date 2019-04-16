import sys
import re
import os
import copy
from pprint import pprint


# This function is range function for floating points
# Needed because "range(0.5, 10.5, 0.5)" : Not supported by default range function
def floatRange(stat, end, step):
    # Note: end is inclusive
    while(start <= end):
        yield start
        start+=step

# Unrolls the loop completly
# Replace variables with their values
# Example:
# for i in {1,2,3,4} { A[i] = i; } 
# will be replaced by
#    A[1] = i;  
#    A[2] = i;  
#    A[3] = i;  
#    A[4] = i;  
def replaceVarsinForeach(foreachHead, block):
    block.strip().strip("{").strip("}")
    unrolledBlocks=""

    # greps variable and their values in foreach statement
    #
    # Example 
    #
    # \foreach \from/\to in {B/t4,B/t5,C/t6,C/t7} { block }
    # Variables = {\from, \to}
    # Values {
    #    \from : B, B, C, C
    #    \to : t4, t5, t6, t7
    # }
    x=re.findall("\\\\foreach(.*)in[\s]*{(.*?)}", foreachHead)
    if(x):
        x = x[0]
        if(x[1].__contains__("...")):
            x = x[0]
            variable = x[0].strip()
            varRange = x[1].strip()
            rangeOfVariable = varRange.split(",")
            start = float(rangeOfVariable[0])
            if(isinstance(rangeOfVariable[1],float)):
                # 1,2.....10
                step=float(rangeOfVariable[1])-float(rangeOfVariable[0])
            else:
                # 1.....10
                step=1
            end = float(rangeOfVariable[-1])
            for val in floatRange(start, end, step): 
                remainblock=copy.copy(block)
                remainblock = re.sub("\\"+variable.strip(), str(val), remainblock)
                unrolledBlocks += remainblock + "\n"
        else:
            varList=x[0].split("/")
            var_index_to_name ={}
            rangeOfVariables = x[1].strip().split(",")
            for i, var in enumerate(varList):
                var_index_to_name[i] = var.strip().strip("\\")
            # \x/\y in 1/2,3/4,5/6,7/8
            # its like x and y pairwise (1,2) then (3,4) then so on
            for rangeValues in rangeOfVariables:
                remainblock=copy.copy(block)
                for i, val in enumerate(rangeValues.strip().split("/")):
                    # Subsitute variable with its value in entire block
                    remainblock = re.sub("\\\\"+var_index_to_name[i], val, remainblock)
                unrolledBlocks += remainblock + "\n"
    return unrolledBlocks


# Find Foreach block in code and then copy blocks and in each block replace variables by their values
def parseAndHandleForEach(tikzBlock):
    # Find all the foreach and its corresponding block in tikz code and call the replaceVars function
    # \foreach \from/\to in {B/t4,B/t5,C/t6,C/t7} 
    #     block
    # Not block may contain foreach statement
    regexForForeach = re.compile("\\\\foreach.*?in[\s]*{.*?}[\s]*", re.MULTILINE)
    firstForeach = re.finditer(regexForForeach, tikzBlock).next()
    if(not firstForeach):
        return tikzBlock
    block=""
    paraenthesis = 0
    startswithParaenthesis = False
    startOffset = 0
    if(tikzBlock[firstForeach.end(0)] == '{'):
        block+="{"
        paraenthesis=1
        startswithParaenthesis=True
        startOffset = 1
       
    for char in tikzBlock[firstForeach.end(0)+startOffset:]:
        block+=char
        if(char=="{"):
            paraenthesis+=1
        elif(char=="}"):
            paraenthesis-=1
            if(paraenthesis==0 and startswithParaenthesis):
                break
        elif(char==";" and paraenthesis==0):
            break
    return tikzBlock[:firstForeach.start(0)] + replaceVarsinForeach(tikzBlock[firstForeach.start(0): firstForeach.end(0)], block) + tikzBlock[firstForeach.end(0)+len(block):]

if __name__ == "__main__":    
    # fileName = "TestCases/rg-v2.tex"
    directory="TestCases"
    filename="edge-editing-v2.tex"
    fileNameWithPath=directory+"/"+filename
    with open(fileNameWithPath) as inputFile:
        fileContent = inputFile.read()
    regextToGetTikzPictureCode = re.compile("\\\\end[\s]*{tikzpicture}", re.MULTILINE)
    i = -1
    for block in regextToGetTikzPictureCode.split(fileContent):
        if(block.__contains__("tikzpicture")):
            for codeInsideTikzPicture in (re.split("\\\\begin{tikzpicture}", block)):
                i += 1
                if(i%2==1):
                    print "==========================================="
                    print("\nCalling parseAndHandleForEach for:\n")
                    print(codeInsideTikzPicture)
                    print "===========================================\n"
                    _oneforeachRemoved = parseAndHandleForEach(codeInsideTikzPicture)
                    while(_oneforeachRemoved.count("\\foreach")>0):
                        _oneforeachRemoved = parseAndHandleForEach(_oneforeachRemoved)
                    unrolledForeachInTikzPart=_oneforeachRemoved
                    j = 0
                    while(os.path.exists(filename + "t" + str(j) + "_unrolled.tex")):
                        j+=1
                    with open(filename + "t" + str(j) + "_unrolled.tex", "w") as outputFile:
                        outputFile.write(unrolledForeachInTikzPart)
                    

