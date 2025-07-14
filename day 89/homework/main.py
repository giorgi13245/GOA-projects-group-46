def solution(dig):
    len5nums = range(99999, 10000, -1)
    for i in len5nums:
        if str(i) in dig:
            return i
        
def descending_order(num):
    x=sorted(str(num))
    y="".join(x)
    return int(y[::-1])

import math
def is_square(n):    
    if n<0:
        return False
    x=math.isqrt(n)
    return x*x==n

def round_to_next5(n):
    while n%5!=0:
        n+=1
    return n

def array_diff(a, b):
    return [i for i in a if i not in b]

def sortme(words):
    return sorted(words, key=str.lower)

def count_repeats(txt):
    res=0
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            res+=1
            
    return res