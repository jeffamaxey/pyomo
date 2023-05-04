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
#
#  This module was originally developed as part of the PyUtilib project
#  Copyright (c) 2008 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  ___________________________________________________________________________


class Factory(object):
    """
    A class that is used to define a factory for objects.

    Factory objects may be cached for future use.
    """

    def __init__(self, description=None):
        self._description = description
        self._cls = {}
        self._doc = {}

    def __call__(self, name, **kwds):
        exception = kwds.pop('exception', False)
        name = str(name)
        if name not in self._cls:
            if not exception:
                return None
            if self._description is None:
                raise ValueError(f"Unknown factory object type: '{name}'")
            raise ValueError(f"Unknown {self._description}: '{name}'")
        return self._cls[name](**kwds)

    def __iter__(self):
        yield from self._cls

    def __contains__(self, name):
        return str(name) in self._cls

    def get_class(self, name):
        return self._cls[name]

    def doc(self, name):
        return self._doc[name]

    def unregister(self, name):
        name = str(name)
        if name in self._cls:
            del self._cls[name]
            del self._doc[name]
    
    def register(self, name, doc=None):
        def fn(cls):
            self._cls[name] = cls
            self._doc[name] = doc
            return cls
        return fn
