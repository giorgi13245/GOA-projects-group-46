def filter_list(l):
    result=[]
    for i in l:
        if type(i) is not str:
            result.append(i)
            
    return result


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


def friend(x):
    
    result=[]

    for i in x:
        if len(i)==4:
            result.append(i)

    return result

def function(a1,a2):
    return "".join(sorted(set(a1+a2)))





