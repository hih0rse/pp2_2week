#Example:
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Example:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#Example:
set1 = {"abc", 34, True, 40, "male"}
#Example:
myset = {"apple", "banana", "cherry"}
print(type(myset))
#Example:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Example:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#Example:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#Example:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Example:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#Example:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#Example:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#Example:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#Example:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#Example:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
#Example:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#Example:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
#Example:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
#Example:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
#Exercise:
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Exercise:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Exercise:
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Exercise:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Exercise:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

