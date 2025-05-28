def get_middle(s):
    for i in s:
        if len(s)%2==1:
            return s[len(s)//2]
        else:
            return s[len(s)//2-1:len(s)//2+1]
        

import math
def factorial(n):
    if n<0 or n>12:
        raise ValueError
    return math.factorial(n)


def reverse_letter(st):
    new_string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in st:
        if i in alphabet:
            new_string += i
    return new_string[::-1]

def gimme(array):
    return array.index(sorted(array)[1])

def angle(n):
    return 180*(n-2)

def arithmetic(a, b, operator):
    operator=operator.lower()
    if operator=="add":
        return a + b
    elif operator=="subtract":
        return a - b
    elif operator=="multiply":
        return a * b
    else:
        return a / b
    

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


def no_odds(val):
    return [i for i in val if i%2==0]

def greet(name): 
    return f"Hello {name.capitalize()}!"

def show_sequence(n):
    x = sum([i for i in range(n+1)])
    y="+".join([str(i) for i in range(n+1)])
    if n<0:
        return f"{n}<0"
    elif n==0:
        return f"0=0"
    
    return f"{y} = {x}"

def filter_list(l):
    result=[]
    for i in l:
        if type(i) is not str:
            result.append(i)
            
    return result

def solution(text, ending):
    return text.endswith(ending)

def maskify(cc):
    if len(cc)<4:
        return cc

    x=len(cc)-4
    return "#"*x+cc[-4:]


def break_chocolate(n, m):
    if n*m==0:
        return 0
    
    return n*m-1





