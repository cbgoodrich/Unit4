#Charlie Goodrich
#10/26/17
#fibonacci.py - prints the fibonacci sequence

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print(fibonacci(10))
