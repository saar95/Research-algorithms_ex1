import inspect
import doctest
import math

"""
Function for example
"""


def f(x: int, y: int, z, t: int):
    return x * y - z + t


"""
The function accepts another function with arguments and activates the function 
only if the arguments are appropriate
return F result.
"""


def safe_call(f, *item_names):
    """
    >>> safe_call(f,1,3,3.5,0)
    -0.5
    >>> safe_call(f,1,3,9,5)
    -1
    >>> safe_call(f,1,3,2*2,7)
    6
    >>> safe_call(f,1-3,3,3.5,0)
    -9.5
    >>> safe_call(f,1-3,3,3.5,0)
    -9.5
    >>> safe_call(f,1,"a",3.5,1)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(f,1,"fff",3.5,"qq")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(f,1,"2",3.5,"7")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(f,'1',2,3.5,7)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    """
    annotations = []
    f_inf = inspect.getfullargspec(f)
    args = f_inf.args
    for j in range(len(args)):
        if f_inf.annotations.__contains__(args[j]):
            annotations.append(f_inf.annotations.get(args[j]))
        else:
            annotations.append("null")

    for j in range(len(item_names)):
        if annotations[j] != "null":
            if type(item_names[j]) != annotations[j]:
                raise Exception("The argument type doesn't fit the function annotations")
                continue
    print(f(*item_names))


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
