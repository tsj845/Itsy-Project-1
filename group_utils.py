from displayio import Group

def setFront(g, index):
    g.insert(0, g.pop(index))

def setBack(g, index):
    g.append(g.pop(index))

def zIndex(g, index, value):
    g.insert(value, g.pop(index))

def setMaxSize(group, size, parent=None):
    g = Group(size)
    for i in range(len(group)):
        g.append(group.pop(0))
    if parent != None:
        i = parent.index(group)
        parent[i] = g
    return g