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






#2




#3
def to_jaden_case(string):
    list=string.split()
    list2=[]
    for i in list:
        i=i.capitalize()
        list2.append(i)
    return " ".join(list2)



#4
def sum_mix(arr):
    sum=0
    
    for i in arr:
        sum+= int(i)
        
    return sum


#5
def array_plus_array(arr1,arr2):
    return sum(arr1)+sum(arr2)


#6
def reverse_words(s):
    x=s.split()
    return " ".join(x[::-1])


#7
def sum_str(a, b):
    return str(int(a or 0)+ int(b or 0))