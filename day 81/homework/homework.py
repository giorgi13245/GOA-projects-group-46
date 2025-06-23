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


def count_bits(n):
    res = ''  

    while n > 0:
        res = str(n & 1) + res
        n >>= 1
        
    return res.count("1")

def kebabize(st):
    res=""
    res1=""
    nums=["0","1",'2',"3","4","5","6","7","8","9"]
    for i in range(len(st)):
        if st[i].isupper():
            res += "-"
            res += st[i].lower()
        else:
            res+=st[i]
            
    for i in res:
        if i not in nums:
            res1+=i
        else:
            continue
            
    return res1[1:] if res1.startswith("-") else res1



def find_children(brigade):
    res=""
    for i in sorted(brigade):
        if i.isupper():
            res+= i
            res+=i.lower()*brigade.count(i.lower())
            
    return res

