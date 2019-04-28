import re
from filterGraphml import *
from grammar.TikzParser import TikzParser


supportedNodeTags = ["nodeID", "X", "Y", "label", "height", "width", "inner_sep", "fill", "edge_color",
		"scale", "shape", "regular_polygon_sides", "rotate", "auto"]

def filterOutNotSupportedNodeTags(propertyDict):
    for k in list(propertyDict):
        if k not in supportedNodeTags:
            del propertyDict[k]

def handleNumbers(input):
    m = re.search('^\s*([0-9/*-+.]+)\s*(?:pt|cm)?\s*$', input)
    if m and len(m.group(1)) > 0 and m.group(1) != ".":
        return m.group(1)
    
    raise Exception("Could not parse {} individual coordinates".format(input))

def handleProperties(ctx:TikzParser.PropertiesContext):
    #properties: individualProperty
    if ctx.getChildCount() == 1:
        k, v = handleIndividualProperty(ctx.getTypedRuleContexts(TikzParser.IndividualPropertyContext)[0])
        if k is None:
            return {}
        else:
            return {k: v}

    #properties: individualProperty ',' properties
    else:
        k, v = handleIndividualProperty(ctx.getTypedRuleContext(TikzParser.IndividualPropertyContext, 0))
        listProperties = handleProperties(ctx.getTypedRuleContext(TikzParser.PropertiesContext, 0))

        # If same property is present, the later one is given precedence
        if k not in listProperties:
            listProperties[k] = v
        
        return listProperties

def handleIndividualProperty(ctx:TikzParser.IndividualPropertyContext):
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
        k, v = identifyKeyValueProperty(key, value)
    # individual property of format "x"
    else:
        k, v = identifyIndividualProperty(value)

    return k, v