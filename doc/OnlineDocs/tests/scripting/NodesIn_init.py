def NodesIn_init(model, node):
    return [i for i, j in model.Arcs if j == node]
model.NodesIn = Set(model.Nodes, initialize=NodesIn_init)
