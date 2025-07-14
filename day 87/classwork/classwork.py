def capitalize(s):
    res=""
    res1=""
    res2=[]
    if s==[]:
        return ['', '']
    
    for i in range(len(s)):
        if i==0 or i%2==0:
            res+=s[i].upper()
        else:
            res+=s[i]
            
    for k in range(len(s)):
        if k==0 or k%2==0:
            res1 += s[k]
        else:
            res1 += s[k].upper()
            
    
    res2.append(res)
    res2.append(res1)
    return res2


import math
def square_or_square_root(arr):
    res = []
    for num in arr:
        sqrt =  math.sqrt(num)
        if sqrt == int(sqrt):
            res.append(sqrt)
        else:
            res.append(num ** 2)
            
    return res

def solution(nums):
    if nums==None:
        return []
    return sorted(nums)

def number(lines):
    dict=[]
    if lines==[]:
        return []
    for i in range(len(lines)):
        dict.append(f"{i+1}: {lines[i]}")
        
    return dict

def nth_even(n):
    return 2 * (n - 1)

def odd_or_even(arr):
    if sum(arr)%2==0:
        return "even"
    else:
        return "odd"