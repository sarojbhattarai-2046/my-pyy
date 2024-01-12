# unorder neat list of elements / does not contain duplicate elements

x = set()

# we don't create set with set leteral like

y = { 34, 3, 2, 2 }

print(y) # 34, 3, 2

# x.add(4)
# x.remove(34)
2 in y # checks if 2 is in the set

# set is ver fast when we need to look up

z = { 35, 2, 8 }

print(x.intersection(z))
print(x.union(z))
print(x.difference(z))