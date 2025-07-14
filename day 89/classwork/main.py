def factorial(n):
    num=1
    for i in range(1,n+1):
        num *= i
    return num

def matrix_addition(a, b):
    for i in range(len(a)):
        for k in range(len(a[0])):
            a[i][k] += b[i][k]
    return a

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

def is_isogram(str):
    a=str.lower()
    return len(a)==len(set(a))

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