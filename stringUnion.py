#Charlie Goodrich
#10/18/18
#stringUnion.py - tells you the letters in two words

def stringUnion(word1, word2):
    total = " "
    for ch in word1:
        if not ch in total:
            total += ch
            
    for ch in word2:
        if not ch in total:
            total += ch
    
    return total

total = stringUnion("mississippi", "pennsylvania")
print(total)