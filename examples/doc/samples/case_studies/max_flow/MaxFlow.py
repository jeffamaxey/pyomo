from pyomo.core import *

model = AbstractModel()

model.nodes = Set()
model.arcs = Set(within=model.nodes*model.nodes)
model.sources = Set(within=model.nodes)
model.sinks = Set(within=model.nodes)
model.upperBound = Param(model.arcs)
model.supply = Param(model.sources)
model.demand = Param(model.sinks)
model.amount = Var(model.arcs, within=NonNegativeReals)

def totalRule(model):
    return sum(model.amount[i, j] for (i, j) in model.arcs if j in model.sinks)

model.maxFlow = Objective(rule=totalRule, sense=maximize)

def maxRule(model, arcIn, arcOut):
    return (model.amount[arcIn, arcOut] <= model.upperBound[arcIn, arcOut])

model.loadOnArc = Constraint(model.arcs, rule=maxRule)

def flowRule(model, node):
    if node in model.sources:
        flow_out = sum(
          model.amount[i,j]
          for (i,j) in model.arcs
          if i == node
        )
        return ( flow_out <= model.supply[node] )

    elif node in model.sinks:
        flow_in = sum(
          model.amount[i,j]
          for (i,j) in model.arcs
          if j == node
        )
        return (flow_in >= model.demand[node])

    else:
        amountIn = sum(
          model.amount[i,j]
          for (i,j) in model.arcs
          if j == node
        )
        amountOut = sum(
          model.amount[i,j]
          for (i,j) in model.arcs
          if i == node
        )
        return ( amountIn == amountOut )

model.flow = Constraint(model.nodes, rule=flowRule)
