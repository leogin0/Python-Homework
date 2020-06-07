def add(a,b):
    return a+b


def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


def div(a,b):
    return a/b


def calc(fn,a,b):
    return fn(a,b)

print(calc(add,1,2))
print(calc(sub,1,2))
print(calc(mul,1,2))
print(calc(div,1,2))
