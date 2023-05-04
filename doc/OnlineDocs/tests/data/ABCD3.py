from pyomo.environ import *

model = AbstractModel()

model.Z = Set(dimen=3)
model.D = Param(model.Z)

instance = model.create_instance('ABCD3.dat')

print(f'Z {str(sorted(list(instance.Z.data())))}')
print('D')
for key in sorted(instance.D.keys()):
    print(f"{name(instance.D, key)} {str(value(instance.D[key]))}")
