def encode(st):
    res=[]
    vows={
        "a" : "1",
        "e" : "2",
        "i" : "3",
        "o" : "4",
        "u" : "5"
    }
    
    for i in st:
        if i not in vows:
            res.append(i)
        else:
            res.append(vows[i])
    return "".join(res)
    
def decode(st):
    res1=[]
    vows1={
        "1":"a",
        "2":"e",
        "3":"i",
        "4":"o",
        "5":"u"
    }
    
    for i in st:
        if i not in vows1:
            res1.append(i)
        else:
            res1.append(vows1[i])
    return "".join(res1)

def sortme(words):
    return sorted(words, key=str.lower)