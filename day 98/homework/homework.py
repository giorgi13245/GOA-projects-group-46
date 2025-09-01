def missing_values(seq): 
    x = 0
    y = 0
    for i in seq:
        if seq.count(i) == 1:
            x = i
        if seq.count(i) == 2:
            y = i
    return x * x * y


def discover_original_price(n, p):
    return round(n * 100 / (100 - p), 2)


def change(st):
    new = ""
    st = st.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in st:
            new += "1"
        else:
            new += "0"
    return new


def count_bits(n):
    res = ''  

    while n > 0:
        res = str(n & 1) + res
        n >>= 1
        
    return res.count("1")


def count_repeats(txt):
    res=0
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            res+=1
            
            
            
    return res