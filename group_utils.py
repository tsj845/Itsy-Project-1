def setFront(g, index):
    g.insert(0, g.pop(index))

def setBack(g, index):
    g.append(g.pop(index))

def zIndex(g, index, value):
    g.insert(value, g.pop(index))