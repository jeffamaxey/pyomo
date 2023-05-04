def Z_init(model, i):
    return Set.End if i > 10 else 2*i+1
model.Z = Set(initialize=Z_init)
