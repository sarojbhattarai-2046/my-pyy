def func(x, y):
    print(x, y)

pairs = [ (1, 3), (3, 4)]

for par in pairs:
    func(*par)

# * will unpack the array or any kind of list