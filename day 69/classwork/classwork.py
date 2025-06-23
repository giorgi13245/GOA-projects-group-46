def printer_error(s):
    x="abcdefghijklm"
    res = 0
    
    for i in s:
        if i not in x:
            res +=1
            
    return f"{res}/{len(s)}"

def dont_give_me_five(start,end):
    res=[]
    for i in range(start, end+1):
        if "5" not in str(i):
            res.append(i)
            
    return len(res)

def triangular(n):
    if n<0:
        return 0
    return n*(n+1)//2

def is_sorted_and_how(arr):
    if arr==sorted(arr):
        return "yes, ascending"
    elif arr==sorted(arr)[::-1]:
        return "yes, descending"
    else:
        return "no"
    

def bumps(road):
    x=road.lower()
    y=x.count("n")
    
    if y<=15:
        return "Woohoo!"
    else:
        return "Car Dead"