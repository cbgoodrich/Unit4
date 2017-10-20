#Charlie Goodrich
#10/20/17
#stringIntersect.py - prints out the letters in both strings

def stringIntersect("word1", "word2"):
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
