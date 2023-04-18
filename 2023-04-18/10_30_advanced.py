
from functools import wraps
def say(text):
    def _say(func):
        @wraps(func)
        def __say(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)
        
        return __say
    return _say

@say('Hello')
def add(a,b):
    return a+b

print(add(4,5))

# Alternative
def add(a,b):
    return a+b
add = say('Hello')(add)

print(add(2,3))


@say('Hello')
@say('Goodbye')
def add(a,b):
    return a+b
 
print(add(4,5))


# Callable

print(sum([1,2,3]))
print(int('0'))

print(type(sum))
print(type(int))

print(callable(sum))
print(callable(int))


# Decorator in a class
class CallCounter:
    def __init__(self) -> None:
        self.count = 0
        
    def __call__(self):
        self.count += 1
        
c = CallCounter()

print(c.count)
c()

print(c.count)
print(callable(c))

class Say:
    def __init__(self, text) -> None:
        self.text = text
        
    def __call__(self, func):
        @wraps(func)
        def say(*args, **kwargs):
            print(self.text)
            return func(*args, **kwargs)
        return say
    
@Say('Class Hello')
@Say('Class Bye')
def add(a,b):
    return a+b

print(add(4,5))



# Argument check

import functools

def check(*argtypes):
    """Function argument type checker.
    """

    def _check(func):
        """Takes the function.
        """

        @functools.wraps(func)
        def __check(*args):
            """Takes the arguments
            """
            if len(args) != len(argtypes):
                msg = f'Expected {len(argtypes)} but got {len(args)} arguments'
                raise TypeError(msg)
            for arg, argtype in zip(args, argtypes):
                if not isinstance(arg, argtype):
                    msg = f'Expected {argtypes} but got '
                    msg += f'{tuple(type(arg) for arg in args)}'
                    raise TypeError(msg)
            return func(*args)
        return __check
    return _check


@check(float, float)
def add(a, b):
    return a + b

print(add(3., 4.))


# Registering
"""A function registry.
"""

import functools

registry = {}


def register_at_call(name):
    """Register the decorated function at call time.
    """

    def _register(func):
        """Takes the function.
        """

        @functools.wraps(func)
        def __register(*args, **kwargs):
            """Takes the arguments.
            """
            registry.setdefault(name, []).append(func)
            return func(*args, **kwargs)
        return __register
    return _register


def register_at_def(name):
    """Register the decorated function at definition time.
    """

    def _register(func):
        """Takes the function.
        """
        registry.setdefault(name, []).append(func)

        return func
    return _register


@register_at_call('simple')
def add(a, b):
    return a + b

print(registry)
add(7,4)
print(registry)
registry.clear()
print(registry)

@register_at_def('complex')
def add(a, b):
    return a + b

print(registry)
add(7,4)
print(registry)
registry.clear()
print(registry)
