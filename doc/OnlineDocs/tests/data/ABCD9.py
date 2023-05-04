from pyomo.environ import *
import pyomo.common
import sys

model = AbstractModel()

model.Z = Set(dimen=3)
model.Y = Param(model.Z)

try:
    instance = model.create_instance('ABCD9.dat')
except pyomo.common.errors.ApplicationError as e:
    print(f"ERROR {str(e)}")
    sys.exit(1)

print(f'Z {str(sorted(list(instance.Z.data())))}')
print('Y')
for key in sorted(instance.Y.keys()):
    print(f"{instance.Y[key]} {str(value(instance.Y[key]))}")
