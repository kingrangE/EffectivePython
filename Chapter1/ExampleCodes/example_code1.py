"""
It contains code related with whitespace contents
"""

# 1. Using 4 space

def test():
    print("Hello World") # <- this line have to start with 4 spaces

# 4. In a file, **Functions and classes** should be **separated by two blank lines**
class SayHello():
    def print():
        print("Hello")
# it separated by
# two blank like this
def func1():
    print("Hellow World")
    
# 5. In a class, methods should be separated by one blank lines
class Test():
    def print_inform():
        print("It's test function")
    # methods are separated by one blank like this
    def calc(a):
        a += 5
        return a
    
# 6. In dictionary, Don't put space between each key and colon, and put a single space before the corresponding value 
dic = {"kingrangE": "It means that tiger is king"} # like this. Don't put space between key and colon, but put a single space before value
print(dic["kingrangE"])

# 7. Put one space and one space before and after the = operator(assignment)
a = 123 # like this. Put one space and one space before and after the = operator

# 8. For type annotations, ensure that there is no separation between the variable name and the colon, and use a space before the type information
## in function
def add_number(a: int, b: int) -> int:
    return a+b
## in variable
num: int = 5
name: str = "kingrangE"
numbers: list[int] = [1,2,3,4,5]
means: dict[str,str] = {'kingrangE': 'It means that tiger is king.'}
