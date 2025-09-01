def bmi(weight, height):
    bmi = weight/height**2
    if bmi>30:
        return "Obese"
    elif bmi<=30 and bmi>25:
        return "Overweight"
    elif bmi<=25 and bmi>18.5:
        return "Normal"
    else:
        return "Underweight"
    

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


def get_average(marks):
    return sum(marks) // len(marks)


def remove_every_other(list):
    return [list[i] for i in range(0,len(list),2)]


def str_count(strng, letter):
    return strng.count(letter)


def between(a,b):
    return [i for i in range(a,b+1)]


def correct(s):
    s=s.replace("0", "O")
    s=s.replace("5", "S")
    s=s.replace("1", "I")
    return s


def solution(nums):
    if nums==None:
        return []
    return sorted(nums)


def arithmetic(a, b, operator):
    operator=operator.lower()
    if operator=="add":
        return a + b
    elif operator=="subtract":
        return a - b
    elif operator=="multiply":
        return a * b
    else:
        return a / b
    

def odd_count(n):
    lst = range(1,n,2)
    return len(lst)


def two_sort(array):
    return "***".join(sorted(array)[0])