#1
def generate_range(start, stop, step):
    list=[]
    for i in range(start,stop+1,step):
        list.append(i)
    return list



#2



#3
def sum_array(arr):
    if arr==None or arr==[] or len(arr)==1:
        return 0
    else:
        return sum(arr)-min(arr)-max(arr)


#4
def count_by(x, n):
    list=[]
    for i in range(x,x*n+1,x):
        list.append(i)
    return list

