# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# with comprehension 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

# it's like looping through for loop via [ x (for loop)]
# [ x for x in something and some condition(if applicable)]
print(newlist)