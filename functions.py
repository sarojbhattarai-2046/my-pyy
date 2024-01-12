def func(x, y, z = None):
    print('my function', x, y)
    return x * y, x / y # returns tuple if there is multiple return value

r1, r2 = func(5, 6)

# kwargs - key words argument
def func(*args, **kwargs):
    print(args, kwargs) # (1, 2, 3), { key1: 23, key2: 24 }

func(1, 2, 3, key1 = 23, key2 = 24)

x = [ 1, 23, 23636, 2727 ]

print(*x) # 1, 23, 23636, 2727 (now within the square)

def func (x, y):
    print(x,y)

pairs = [ (1,2), (3,4)]

for pair in pairs:
    func(*pair)