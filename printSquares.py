#Charlie Goodrich
#10/17/17
#printSquares.py - prints a grid of squares

def printSquares(rows, columns):
    for j in range(1, columns + 1):
        print("+--" *rows + "+")
        print("|  " *rows + "|")
        
    print("+--" *rows + "+")
    
printSquares(5,5)
