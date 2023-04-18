class C:

    def meth(self):
        return 42
        
    def func():
        return 42

    func = staticmethod(func)
    
c = C()
print(c.func())
print(c.meth())


class C2:

    def meth(self):
        return 42
       
    @staticmethod 
    def func():
        return 42
      
c = C2()
print(c.func())
print(c.meth())  


# Closure

def outer(arg1):
    def inner(arg2):
        return arg1 + arg2

    return inner

i10 = outer(10)
print(i10(4))


# Simple Decorator

def hello(func):
    def wrapper(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)
    
    return wrapper

@hello
def add(a, b):
    """Add two objects."""
    return a + b

print(add(4, 5))

print(add.__doc__)
print(add.__name__)


# ARGS / KWARGS

def func(*args):
    print(args)

func(1)


def func(**kwargs):
    print(kwargs)

func(a=2, b=5)


def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1,2,3, a=2, b=5)


L = [1, 2, 3]

print(*L)


# Simple Decorator with functools wraps

from functools import wraps
def hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)
    
    return wrapper


@hello
def add(a, b):
    """Add two objects."""
    return a + b

print(add(4, 5))

print(add.__doc__)
print(add.__name__)


# Blick auf die cached.py

import functools
import pickle


def cached(func):
    """Decorator that caches.
    """
    cache = {}

    @functools.wraps(func)
    def _cached(*args, **kwargs):
        """Takes the arguments.
        """
        # dicts cannot be use as dict keys
        # dumps are strings and can be used
        key = pickle.dumps((args, kwargs))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return _cached


@cached
def add(a, b):
    print('adding')
    return a+b

print(add(1,2))
print(add(3,4))

print(add.__wrapped__)


# Blick auf die logged.py
# Decorator for logging 

LOGGING = False


def logged(func):
    """Decorator for logging.
    """

    @functools.wraps(func)
    def _logged(*args, **kwargs):
        """Takes the arguments
        """
        if LOGGING:
            print('logged') # do proper logging here
        return func(*args, **kwargs)
    return _logged

@logged
def add(a, b):
    return a+b

print(add(1,2))

LOGGING = True

print(add(1,2))
