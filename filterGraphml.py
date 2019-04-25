from colour import Color
import logging
logger = logging.getLogger(__name__)

ValidNodeShapes = ["rectangle", "circle", "diamond", "ellipse", "regular polygon"]
ValidEdgeDirections = ["->", "<-"]  #- means no edge. So no need to check for its validity as that is default

def isValidColor(value):
    #If value contains ! then it is definatly color (not seem ! in any other variable/property)
    if value.__contains__("!"):
        return True
    # Check if we can get color object of given value or not
    try:
        Color(value)
        return True
    except:
        return False

def isValidShape(value):
    if value in ValidNodeShapes:
        return True
    return False

def isValidDirection(value):
    if value in ValidEdgeDirections:
        return True
    return False

# Refer http://www.texample.net/tikz/examples/node-shapes/
# for Tikz shapes
def identifyShape(value):
    if value in ValidNodeShapes:
        return value
    return None

def identifyIndividualProperty(value):
    value = value.strip().lower()
    if isValidColor(value):
        return ("fill", value)
    elif isValidShape(value):
        return ("shape", value)
    elif isValidDirection(value):
        return ("direction", value)
    #Add other checks here

    # We could not identify what property it was so return none
    logger.warning("Got Unhandled Property, Ignoring it for now ({})".format(value))
    return (None, None)

def identifyKeyValueProperty(key:str, value:str):
    key, value = key.strip().lower(), value.strip().lower()

    if key == "shape":
        return (key, identifyShape(value))

    elif key in ["fill", "rotate", "label"]:
        return (key, value)

    elif key == "inner sep":
        return ("inner_sep", value)
    
    elif key == "regular polygon sides":
        return ("regular_polygon_sides", value)

    
    #Add other checks here

    logger.warning("Got Unhandled Property, Ignoring it for now ({},{})".format(key, value))
    return None, None


