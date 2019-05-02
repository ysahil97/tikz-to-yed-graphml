import re
import logging
import tikz2graphml.filterGraphml as filterGraphml
from tikz2graphml.grammar.TikzParser import TikzParser

logger = logging.getLogger()

supportedNodeTags = ["nodeID", "X", "Y", "label", "height", "width", "inner_sep", "fill", "edge_color",
                     "scale", "shape", "regular_polygon_sides", "rotate", "auto"]

def filterOutNotSupportedNodeTags(propertyDict):
    for k in list(propertyDict):
        if k not in supportedNodeTags:
            del propertyDict[k]

# Handle Parsing of label strings obtained from Antlr
def parseLabelValue(labelstr):

    if labelstr[0] != '{':
        raise Exception("Expected '{' at the beginning of label. Label starts with incorrect bracket. Got " + labelstr)

    new_label_str = labelstr[1:]
    slice_index = -1
    for i in range(len(new_label_str)-1, -1,-1):
        if new_label_str[i] == '}':
            slice_index = i
            break
        else:
            continue

    if slice_index == -1:
        raise Exception("Expected '};' at the end of label. Got " + labelstr)

    return new_label_str[:slice_index]

# Number handling. Also handles floats
def handleNumbers(input):
    m = re.search('^\s*([0-9/*-+.]+)\s*(?:(pt|cm))?\s*$', input)
    try:
        if m and len(m.group(1)) > 0 and m.group(1) != ".":
            if m.group(2) and m.group(2) == "cm":
                return float(eval(m.group(1)))
            return float(eval(m.group(1)))
    except:
        raise Exception("Cannot Evaluate Math Expression {}".format(input))

# Parses a list of property strings and retures a dictionary of those properties
def handleProperties(ctx: TikzParser.PropertiesContext):
    # properties: individualProperty
    if ctx.getChildCount() == 1:
        k, v = handleIndividualProperty(ctx.getTypedRuleContexts(TikzParser.IndividualPropertyContext)[0])
        if k is None:
            return {}
        else:
            return {k: v}

    # properties: individualProperty ',' properties
    else:
        k, v = handleIndividualProperty(ctx.getTypedRuleContext(TikzParser.IndividualPropertyContext, 0))
        listProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))

        # If same property is present, the later one is given precedence
        if k not in listProperties:
            listProperties[k] = v

        return listProperties

def handleIndividualProperty(ctx: TikzParser.IndividualPropertyContext):
    key = ""
    value = ""
    currentValue = ""
    for child in ctx.children:
        if child.getText() != "=":
            currentValue += child.getText() + " "
        else:
            key = currentValue
            currentValue = ""
    value = currentValue
    # property of Key Value of format "x = y"
    if len(key) > 0:
        k, v = filterGraphml.identifyKeyValueProperty(key, value)
    # individual property of format "x"
    else:
        k, v = filterGraphml.identifyIndividualProperty(value)

    return k, v
