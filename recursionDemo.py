#Charlie Goodrich
#10/26/17
#recursionDemo.py - a recursive verson of the countdown function

def countdown(n):
    if n == 0:
        print("BOOM!")
    else:
        print(n)
        countdown(n-1)
    
countdown(10)
