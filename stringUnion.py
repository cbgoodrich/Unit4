#Charlie Goodrich
#10/18/18
#stringUnion.py - tells you the letters in two words

def stringUnion(word1, word2):
    total = " "
    for ch in word1:
        if ch in word1 and ch in word2:
            return ch
    
print(stringUnion("high", "height"))
