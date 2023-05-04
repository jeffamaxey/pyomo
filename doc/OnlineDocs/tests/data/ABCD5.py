from pyomo.environ import *

model = AbstractModel()

# @decl
model.Z = Set()
model.Y = Param(model.Z)
model.W = Param(model.Z)
# @decl

instance = model.create_instance('ABCD5.dat')

print(f'Z {str(sorted(list(instance.Z.data())))}')
print('Y')
for key in sorted(instance.Y.keys()):
    print(f"{name(instance.Y, key)} {str(value(instance.Y[key]))}")
print('W')
for key in sorted(instance.W.keys()):
    print(f"{name(instance.W, key)} {str(value(instance.W[key]))}")
