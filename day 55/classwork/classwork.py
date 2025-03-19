#problem1

dict1={
    "name":"mercedes",
    "brand":"G class",
    "year":2020
}

print(dict1.items())
print(dict1.keys())
print(dict1.values())

#problem2

set3={1,2,3,4,5}
set2={6,5,2,7,8}

print(set3 | set2)
print(set3.symmetric_difference(set2))
print(set3.intersection(set2))


#problem3

dict2={
    "name":"giorgi",
    "lastname":"boyoveli",
    "age":15
}

for i in dict2.values():
    print(i)


#problem4

#dict და set ორივე იწერება კლაკნილი ფრჩხილებით, მათზე არ მუშაობს ინდექსები, dict არის ordered, set კი არა



#problem5


dict3={
    "n1":1,
    "n2":2,
    "n3":3, 
}

list1=[]

for i in dict3.items():
    list.append(i)

print(list1)