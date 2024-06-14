#Example:
print(10 + 5)
#Example:
print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
#Example:
print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

#Example:
print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""

#Exercise:
print(10 * 5)
#Exercise:
print(10 / 2)
#Exercise:
fruits = ["apple", "banana"]
if "apple" in fruits:  
    print("Yes, apple is a fruit!")
#Exercise:
if 5 != 10:
  print("5 and 10 is not equal")
#Exercise:
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")