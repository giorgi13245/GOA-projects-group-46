#N1
dict1={
    "food":"apple",
    "car":"mercedes",
    "money":"500k"
}

list1=[]
list2=[]

for i in dict1.keys():
    list1.append(i)

for k in dict1.values():
    list2.append(k)

print(list1)
print(list2)

#N2
result=[10,43,12,11,94,10,55,7,11]
print(list(set(result)))


#N3
input1=input("enter key")
input2=input("enter value")
input3=input("enter new value")


dict2={
    input1:input2
}

dict2[input1]=input3

print(dict2)

#N4
def setSim(lst):
    list4=[]
    for i in lst:
        if i not in list4:
            list4.append(i)
    return list4

print(setSim([1,2,3,4,1,2,9,1,2]))
            
