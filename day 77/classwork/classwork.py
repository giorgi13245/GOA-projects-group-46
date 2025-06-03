def arithmetic(a, b, operator):
    if operator=="add":
        return a + b
    elif operator=="subtract":
        return a - b
    elif operator=="multiply":
        return a * b
    else:
        return a / b
    

def is_anagram(test, org):
    return sorted(test.lower())==sorted(org.lower())


def count_by(x, n):
    list=[]
    for i in range(x,x*n+1,x):
        list.append(i)
    return list


def other_angle(a, b):
    return 180-a-b

def sum_even_numbers(seq): 
    return sum(i for i in seq if i%2==0)

def human_years_cat_years_dog_years(human):
    x=human-2
    if human==0:
        return [0,0,0]
    elif human==1:
        return [1,15,15]
    return [human,15+9+4*x,15+9+5*x]

def sum_str(a, b):
    return str(int(a or 0)+ int(b or 0))

def remove_smallest(nums):
    if nums==[]:
        return []
    x=min(nums)
    y=nums.index(x)
    num1=nums.copy()
    num1.pop(y)
    return num1