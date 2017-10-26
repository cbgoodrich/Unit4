#Charlie Goodrich
#10/26/17
#factorial.py - a recursive way to do factorials


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
