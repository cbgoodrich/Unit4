#Charlie Goodrich
#10/16/17
#countdown.py - prints the countdown

def countdown():
    n = int(input("Enter the number you want to countdown from: "))
    for i in range(n, 0, -1):
        print(i)
    print("BOOM!")
countdown()
