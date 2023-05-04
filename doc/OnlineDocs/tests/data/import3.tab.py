from pyomo.environ import *

model = AbstractModel()

model.A = Set()

instance = model.create_instance('import3.tab.dat')

print(f'A {str(sorted(list(instance.A.data())))}')
