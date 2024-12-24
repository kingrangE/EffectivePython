"""
It contains code related with Expressions contents
"""

# 1. Use inline negation 
name ="kingrangE"

if name is not "kingrangE" : #Recommend
    print("Recommend")

if not name is "kingrangE" : #Do not this
    print("Do not this!")

# 2. Don't check for empty and non-empty containers or sequences

empty = []
non_empty = [1,2,3]

if empty :
    print("Recommend this method")

if non_empty :
    print("Recommend this method")

if len(empty) != 0 : 
    print("Do not this!")

if len(non_empty) > 0 :
    print("Do not this!")

# 3. Avoid single-line if statement
T = True
F = False
## if
if T : 
    print("Recommend this method")
if T : print("Do not this!") 

## for
for i in range(2):
    print("Recommend this method")
for i in range(2): print("Do not this!")

## while
while T :
    print("Recommend this method")
    break
while T : print("Do not this!"); break

## except
try :
    print("Recommend this method")
except Exception:
    print("Good")

try:print("Do not this!")
except Exception:print("Bad")

# 4. use paranthese
print("Recommend this method")
a = (1+2+3+4+
    5+6+7+9)
a = (
    1+2+3+4
    +5+6+7+8
)

print("Do not use the following method")
a = 1+2+3+4+\
    5+6+7+9
