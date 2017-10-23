#Charlie Goodrich
#10/23/17
#warmup11.py - tells you if you've got a prime number

def isPrime(number):
    if number>2:
        for i in range(2, number//2 + 1):
            if number%i == 0:
                return False
        return True
    else:
        return True
print(isPrime(9))