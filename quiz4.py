#Charlie Goodrich
#10/30/17
"""quiz4.py - prints out CSIA four times, returns the average of 3 numbers
prints the last letter of a word, returns True or False for two arguments"""

def csia():
    print("Computer Science is Awesome "*5)

csia()

def average(num1, num2, num3):
    return (num1 + num2 + num3)/3
    
print(average(1,2,3))

def lastLetter(word):
    print("e") #how do you do this
lastLetter("Charlie")


def same(exp1, exp2):
    if exp1 == exp2:
        return True
    else:
        return False
print(same(2*2, 7-1))

