#Charlie Goodrich
#10/16/17
#printnStars.py - prints the number of stars

def printnStars():
    i = 1
    n = int(input("Enter number of stars: "))
    while i <= n:
        print("*"*i)
        i += 1

printnStars()