import re
import copy
import logging

logger = logging.getLogger()

# This function is range function for floating points
# Needed because "range(0.5, 10.5, 0.5)" : Not supported by default range function
def floatRange(start, end, step):
    # Note: end is inclusive
    while(start <= end):
        yield start
        start += step

# Unrolls the loop completely
# Replace variables with their values
# Example:
# for i in {1,2,3,4} { A[i] = i; } 
# will be replaced by
#    A[1] = i;  
#    A[2] = i;  
#    A[3] = i;  
#    A[4] = i;  
def replaceVarsinForeach(foreachHead, block):
    block = block.strip().strip("{").strip("}")
    unrolledBlocks = ""
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
    x = re.findall("\\\\foreach(.*)in[\s]*{(.*?)}", foreachHead)
    if(x):
        x = x[0]
        if(x[1].__contains__("...")):
            variable = x[0].strip()
            varRange = x[1].strip()
            rangeOfVariable = varRange.split(",")
            start = float(rangeOfVariable[0])
            if(isinstance(rangeOfVariable[1], float)):
                # 1,2.....10
                step = float(rangeOfVariable[1])-float(rangeOfVariable[0])
            else:
                # 1.....10
                step = 1
            end = float(rangeOfVariable[-1])
            for val in floatRange(start, end, step): 
                remainblock = copy.copy(block)
                remainblock = re.sub("\\"+variable.strip(), str(val), remainblock)
                unrolledBlocks += remainblock.strip() + "\n"
        else:
            varList = x[0].split("/")
            var_index_to_name = {}
            rangeOfVariables = x[1].strip().split(",")
            for i, var in enumerate(varList):
                var_index_to_name[i] = var.strip().strip("\\")
            # \x/\y in 1/2,3/4,5/6,7/8
            # its like x and y pairwise (1,2) then (3,4) then so on
            for rangeValues in rangeOfVariables:
                remainblock = copy.copy(block)
                for i, val in enumerate(rangeValues.strip().split("/")):
                    # Subsitute variable with its value in entire block
                    remainblock = re.sub("\\\\"+var_index_to_name[i], val, remainblock)
                unrolledBlocks += remainblock.strip() + "\n"
    return unrolledBlocks

# Find Foreach block in code and then copy blocks and in each block replace variables by their values
def parseAndHandleForEach(tikzBlock):
    # Find all the foreach and its corresponding block in tikz code and call the replaceVars function
    # \foreach \from/\to in {B/t4,B/t5,C/t6,C/t7} 
    #     block
    # Not block may contain foreach statement
    regexForForeach = re.compile("\\\\foreach.*?in[\s]*{.*?}[\s]*", re.MULTILINE)
    firstForeach = None
    for x in re.finditer(regexForForeach, tikzBlock):
        firstForeach = x
        break
    if not firstForeach:
        return tikzBlock
    block = ""
    parantheses = 0
    startswithParantheses = False
    startOffset = 0
    if tikzBlock[firstForeach.end(0)] == '{':
        block += "{"
        parantheses = 1
        startswithParantheses = True
        startOffset = 1
    for char in tikzBlock[firstForeach.end(0)+startOffset:]:
        block += char
        if char == "{":
            parantheses += 1
        elif char == "}":
            parantheses -= 1
            if parantheses == 0 and startswithParantheses:
                break
        elif char == ";" and parantheses == 0:
            break
    return tikzBlock[:firstForeach.start(0)] + replaceVarsinForeach(tikzBlock[firstForeach.start(0): firstForeach.end(0)], block) + tikzBlock[firstForeach.end(0)+len(block):]

# returns list of blocks with unrolled for loops
# A block is the code inside tikz begin and end
def getCodeInsideTIKZAfterUnrolling(filename):
    tikzBlocks = []
    with open(filename) as inputFile:
        fileContent = inputFile.read()
    regextToGetTikzPictureCode = re.compile("\\\\end[\s]*{tikzpicture}", re.MULTILINE)
    i = -1
    for block in regextToGetTikzPictureCode.split(fileContent):
        if(block.__contains__("tikzpicture")):
            for codeInsideTikzPicture in (re.split("\\\\begin{tikzpicture}", block)):
                i += 1
                if i % 2 == 1:
                    oneforeachRemoved = parseAndHandleForEach(codeInsideTikzPicture)
                    while(oneforeachRemoved.count("\\foreach")>0):
                        oneforeachRemoved = parseAndHandleForEach(oneforeachRemoved)
                    unrolledForeachInTikzPart = oneforeachRemoved
                    tikzBlocks.append("\\begin{tikzpicture}" + unrolledForeachInTikzPart + "\\end{tikzpicture}")
    return tikzBlocks