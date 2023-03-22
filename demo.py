import sys

def add(n, m):
    return n + m

def square(n):
    return n * n

def cube(n):
    return n * n * n

print(cube(int(sys.argv[1])))
