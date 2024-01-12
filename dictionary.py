# key value pair like an object in JS but keys and values can of of any data type

x = {
    'key': 12345
}

# print(x['key'])

# add key

x['new_key'] = 34

# print(x['new_key'])

'key' in x # checks is key exist in dict

print(list(x.values())) # VALUES OF X ([ 12345, 34 ])

# list converts to readable collection like array

# deleting key
del x['key']

for key in x:
    print(key, x['key'])

    