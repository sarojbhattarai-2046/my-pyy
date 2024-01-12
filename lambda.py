x = lambda x,y: x + y

x(1,2)

x = [1, 2, 3, 4, 5]

mp = map(lambda x: x + 2, x)

xx = filter(lambda i: i % 2 == 0, x)

print(list(mp))
print(list(xx))