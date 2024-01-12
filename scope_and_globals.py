x = 'tim'

def func(name):
    x = name # the global x is not changed here because x can be read but can not be modified
    # global x; x = name will change the global x !!! DON'T USE IT

print(x)
print('modified')
print(x)