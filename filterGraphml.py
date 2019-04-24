node_shapes = ["rectangle", "circle", "diamond", "ellipse"]

# Refer http://www.texample.net/tikz/examples/node-shapes/
# for Tikz shapes
def identifyShape(value):
    for shape in node_shapes:
        if value == shape:
            if value == "circle":
                return "ellipse"
            else:
                return value
    return "circle"

def identifyIndividualProperty(value):
    value = value.strip().lower()
    return ("shape", identifyShape(value))

def identifyKeyValueProperty(key:str, value:str):
    key, value = key.strip().lower(), value.strip().lower()
    if key == "shape":
        return key, identifyShape(value)
    else:
        return key, value

