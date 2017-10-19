#Charlie Goodrich
#10/18/18
#stringUnion.py - tells you the letters in two words

def stringUnion(word1, word2):
    total = " "
    for ch in word1:
        total += ch
    for ch in word2:
        total += ch
        
    print(total)
    
stringUnion("high", "kite")
