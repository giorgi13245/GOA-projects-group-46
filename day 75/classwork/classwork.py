def past(h, m, s):
    x=1000*s
    y=60000*m
    z=3600000*h
    
    return x+y+z

def find_needle(haystack):
    index=haystack.index("needle")
    return f"found the needle at position {index}"

def grow(arr):
    result=1

    for i in arr:
        result *=i

    return result

def rental_car_cost(d):
    if d>=7:
        return d*40-50
    elif d>=3:
        return d*40-20
    else:
        return d*40
    

def is_triangle(a, b, c):
    if a<0 or b<0 or c<0:
        return False
    elif a+b<c or a+c<b or b+c<a:
        return False
    elif a+b==c or a+c==b or b+c==a:
        return False
    return True

def stray(arr):
    for i in arr:
        if arr.count(i)==1:
            return i
        

def repeats(arr):
    res=0
    for i in arr:
        if arr.count(i)==1:
            res += i
            
    return res

def sortme(words):
    return sorted(words, key=str.lower)


def hamming(a,b):
    res=0
    for i in range(0,len(a)):
        if a[i] != b[i]:
            res += 1
            
    return res


def delete_nth(order,max):
    res = []
    for i in order:
        if res.count(i)<max:
            res.append(i)
            
    return res

