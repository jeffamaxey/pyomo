from pyomo.environ import *

model = AbstractModel()

model.p = Param()

instance = model.create_instance('import6.tab.dat')

print(f'p {str(value(instance.p))}')
