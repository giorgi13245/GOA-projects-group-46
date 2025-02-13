#1
def capitals(word):
    result=[]
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result


#2
def max_multiple(divisor, bound):
    result=[]
    for i in range(0,bound+1):
        if i%divisor==0:
            result.append(i)
        else:
            continue
        
    return max(result)

#3
def sum_digits(number):
    if number<0:
        number=str(number*-1)
    else:
        number=str(number)
        
    result=0
    for i in number:
        result+=int(i)
    return result


#4
# 





#5
# 

#6
def invert(lst):
    result=[]
    for i in lst:
        result.append(-i)
    return result


#7
def sum_array(arr):
    if arr==None or arr==[] or len(arr)==1:
        return 0
    else:
        return sum(arr)-min(arr)-max(arr)
