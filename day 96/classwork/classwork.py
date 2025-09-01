def to_underscore(strng):
    if type(strng)==int:
        return str(strng)
    
    res=""
    
    for i in range(len(strng)):
        if strng[i].isupper():
            res += "_"
            res += strng[i].lower()
        else:
            res+=strng[i]
            
        
        
        
    return res[1:]


def count_repeats(txt):
    res=0
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            res+=1
            
            
            
    return res

def string_transformer(s):
    s = s.swapcase()
    s = s.split(" ")[::-1]
    s = " ".join(s)
    return s