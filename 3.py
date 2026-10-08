def add(a , b):
    if a + b < 10:
        return a + 1 , b + 1
    else:
        return a + b
print(add(2, 3))