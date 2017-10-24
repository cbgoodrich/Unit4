#Charlie Goodrich
#10/24/17
#multiply.py - helps kids with multiplication

from random import randint

def message():
    print("Watch out world. Here comes the next great multiplier!")

correctCounter = 0
i = 1
while i<6:
    num1 = randint(1, 12)
    num2 = randint(1, 12)
    print(num1, "x", num2, "=")
    guess = int(input("? "))
    ans = num1 * num2
    if guess == ans:
        correctCounter += 1
    if correctCounter == 5:
        message()
    i += 1
    
