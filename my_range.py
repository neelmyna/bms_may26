def my_range(*args):
    # print(type(args))
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif len(args) == 3 and args[2] > 0:
        i = args[0]
        while i < args[1]:
            yield i
            i += args[2]
    elif len(args) == 3 and args[2] < 0:
        i = args[0]
        while i > args[1]:
            yield i
            i += args[2]
    else:
        raise TypeError

for i in my_range(72, 41, -4, 10):
    print(i, end= "  ")