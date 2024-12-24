"""
It contains code related with naming
"""

# 1~6. formats

## 4. module-level constants
PI = 3.14

## 1. variable (using lower case)
name = "kingrangE" 
age = 25
name_to_age = {"kingrangE":age}

## 1. function (using lower case)
def func():
    print("Function should use lower case")
def func_dup():
    print("Function should use lower case")

## class 
class Test():
    class_level_attribute = "I'm class level attribute"
    def __init__(self):
        self.public_attribute = "I'm public attribute" # 1. most of attribute (using lower case)
        self._protected_attribute = "I'm protected attribute" # 2. protected attribute (using _leading_underscore)
        self.__private_attribute = "I'm private attribute" # 3. private attribute (using __double_leading_underscore)
    def show_variables(self): # 5. Instance methods (using lowercase(#1) and should be use self)
        print(self.public_attribute)
        print(self._protected_attribute)
        print(self.__private_attribute)

    @classmethod
    def print(cls): #6. Class methods (using lowercase(#1) and should be use cls)
        print(cls.class_level_attribute)

print("Class method and class-level attributes can be access without creating an instance")
print("Class Method : " ,end="")
Test.print()
print("Class level attribute : ",Test.class_level_attribute)
print("But Instance method can be access after creating an instance")
test = Test()
test.show_variables()

