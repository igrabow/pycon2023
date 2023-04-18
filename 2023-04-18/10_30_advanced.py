
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

from functools import wraps

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

