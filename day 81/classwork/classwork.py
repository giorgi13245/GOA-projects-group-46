def problem(a):
    if type(a)==str:
        return "Error"
    return a*50+6

def is_opposite(s1,s2):
    if s1=="" or s2=="":
        return False
    return s1.swapcase()==s2

def flick_switch(lst):
    res=[]
    x=True
    for i in lst:
        if i=="flick":
            x = not x
            res.append(x)
        else:
            res.append(x)
            
    return res


def if_chuck_says_so():
    return "GOA"=="worst academy" 
#   returns always F+alse

def move_zeros(lst):
    res=[]
    for i in lst:
        if i != 0:
            res.append(i)
            
    for i in lst:
        if i==0:
            res.append(i)
            
    return res

def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)

def alphanumeric(pas):
    if len(pas)==0 or pas=="":
        return False
    elif " " in pas or "_" in pas:
        return False
    
    for i in pas:
        if i.isalnum()==False:
            return False
        
    return True