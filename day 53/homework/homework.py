#N1
# set1={1,2,3}
# set1[1]=4
# set1[2]=5
# set1[3]=6
#it wont work because sets dont have indexes


#N2
set2={"burger","cola","fries"}
set3={"apple","banana","orange"}
set2.clear()
set2.update(set3)
print(set2)

#N3
list2=[5,8,34,67,88,88,67,90,5]
print(list(set(list2)))



