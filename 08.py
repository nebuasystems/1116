#


def asd():
    pass


print(asd)

def times(a, b):
    return a * b

t = times
print(t(100,100))
print(t, times, sep=',')


def print_menu():
    print('1')
    print('2')

print_menu()

print('===================')

def swap(a, b):
    return b, a, 99

c = swap(10 ,20)
print(c, type(c))


print('===================')

def f(t):
    t = 20
    return t
a = 10

print(f(a))

print(a)

print('===================')


def g(t):
    t[0] = 0




a = [ 1, 2, 3]
g(a)
print(a)