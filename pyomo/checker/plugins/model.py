#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2022
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

import ast

from pyomo.common.plugin import SingletonPlugin, implements
from pyomo.checker.hooks import IPreCheckHook


class ModelTrackerHook(SingletonPlugin):

    implements(IPreCheckHook)

    def precheck(self, runner, script, info):
        # create models dict if nonexistent
        if getattr(script, 'modelVars', None) is None:
            script.modelVars = {}

        # parse AST node
        if (
            isinstance(info, ast.Assign)
            and isinstance(info.value, ast.Call)
            and isinstance(info.value.func, ast.Name)
        ):
            for target in info.targets:
                if info.value.func.id.endswith("Model"):
                    if isinstance(target, ast.Name):
                        script.modelVars[target.id] = info.value.func.id
                    elif isinstance(target, ast.Tuple):
                        for elt in target.elts:
                            if isinstance(elt, ast.Name):
                                script.modelVars[elt.id] = info.value.func.id
                elif isinstance(target, ast.Name):
                    if target.id in script.modelVars:
                        del script.modelVars[target.id]
                elif isinstance(target, ast.Tuple):
                    for elt in target.elts:
                        if (
                            isinstance(elt, ast.Name)
                            and elt.id in script.modelVars
                        ):
                            del script.modelVars[elt.id]
