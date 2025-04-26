def to_jaden_case(string):
    list=string.split()
    list2=[]
    for i in list:
        i=i.capitalize()
        list2.append(i)
    return " ".join(list2)


def get_sum(a,b):
    res=[]
    if a==b:
        return a
    elif b>a:
        for i in range(a,b+1):
            res.append(i)
    elif a>b:
        for k in range(b, a+1):
            res.append(k)
            
    return sum(res)


def count_red_beads(n):
    if n<2:
        return 0
    
    return n*2-2


def missing_values(seq): 
    x = 0
    y = 0
    for i in seq:
        if seq.count(i) == 1:
            x = i
        if seq.count(i) == 2:
            y = i
    return x * x * y