#!/user/bin/python
"""
"""
import abc

_notimplemented = abc.abstractproperty(lambda self, *args, **kwargs: NotImplemented)

class WorkflowInterface(object):
    __metaclass__ = abc.ABCMeta

    steps = abc.abstractproperty(_notimplemented)
