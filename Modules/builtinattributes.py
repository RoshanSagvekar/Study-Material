'''
import math
print(math.__dict__)

class myclass(object):
    class_var=1
    def __init__(self,i_var) :
        self.i_var=i_var
foo=myclass(2)
bar=myclass(3)


def demo():
    """
    This is an example of how a doc_string looks like.
    This string give useful information about the function being defined.
    """
print(demo.__doc__)
'''
print("__name__ = ", __name__)

class A:
    pass
class B(A):
    pass
b=B()
print(b.__module__)
print(B.__bases__)