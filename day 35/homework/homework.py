#1
# 



#2
def sequence_sum(begin_number, end_number, step):
    result=0
    list=[]
    if begin_number>end_number:
        return 0
    elif begin_number==end_number:
        return begin_number


    
    for i in range(begin_number, end_number+1, step):
        list.append(i)
    return sum(list)

#3
def lowercase_count(strng):
    result=0
    for i in strng:
        if i.islower():
            result+=1
    return result

#4
def better_than_average(class_points, your_points):
    if your_points>=sum(class_points)/len(class_points):
        return True
    else:
        return False
    

#5
def grow(arr):
    result=1

    for i in arr:
        result *=i

    return result


#6
def smash(words):
    x=" ".join(words)
    return x[::]