#Charlie Goodrich
#10/27/17
#GCF.py - prints the greatest common factor

def GCF(num1, num2):
    small = min(num1, num2)
    for i in range(small, 0, -1):
        if num1%i == 0 and num2%i == 0:
            return i

print(GCF(10,17))
    