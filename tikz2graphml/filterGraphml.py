import logging
from colour import Color

logger = logging.getLogger()

ValidNodeShapes = ["rectangle", "circle", "diamond", "ellipse"]
ValidEdgeDirections = ["->", "<-", "-!-", "--", "<->", "-"]  #- means no edge. So no need to check for its validity as that is default

"""
A list of functions which try to check the validity of each attribute
and optionally defining a default value wherever required
"""

def isValidColor(value):
    # If value contains ! then it is definatly color (not seem ! in any other variable/property)
    if value.__contains__("!"):
        return True
    # Check if we can get color object of given value or not
    try:
        Color(value)
        return True
    except:
        return False

def isValidShape(value):
    return value in ValidNodeShapes

def isValidDirection(value):
    return value in ValidEdgeDirections

# Refer http://www.texample.net/tikz/examples/node-shapes/
# for Tikz shapes
def identifyShape(value):
    return value if value in ValidNodeShapes else "rectangle"

def isValidThickness(value):
    return value.lower() in ["thick", "thin", "ultra thich"]

def isValidEdgeStyle(value):
    return value.lower() in ["dash", "solid", "dotted" ]

def identifyIndividualProperty(value):
    value = value.strip().lower()
    if isValidColor(value):
        return ("fill", value)
    elif isValidShape(value):
        return ("shape", value)
    elif isValidDirection(value):
        return ("direction", value)
    elif isValidThickness(value):
        return ("width", value)
    elif isValidEdgeStyle(value):
        return ("line_type", value)

    # Add other checks here

    # We could not identify what property it was so return none
    logger.warning("Got Unhandled Property, Ignoring it for now ({})".format(value))
    return (None, None)

def identifyKeyValueProperty(key: str, value: str):
    key, value = key.strip().lower(), value.strip().lower()

    if key == "shape":
        return (key, identifyShape(value))

    elif key in ["fill", "rotate", "label"]:
        return (key, value)

    elif key == "inner sep":
        return ("inner_sep", value)

    elif key == "direction":
        return ("direction", value)

    elif key == "thickness" or key == "width":
        return ("width", value)

    elif key == "edgeStyle":
        return ("edgeStyle", value)

    elif key == "edge label":
        return ("label", value)

    elif key == "scale":
        return ("scale", value)

    elif key == "auto":
        return ("auto", value)

    # Add other checks here

    logger.warning("Got Unhandled Property, Ignoring it for now ({},{})".format(key, value))
    return None, None
