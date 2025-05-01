def filter_list(l):
    result=[]
    for i in l:
        if type(i) is not str:
            result.append(i)
            
    return result


def to_jaden_case(string):
    list=string.split()
    list2=[]
    for i in list:
        i=i.capitalize()
        list2.append(i)
    return " ".join(list2)


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


def is_triangle(a, b, c):
    if a<0 or b<0 or c<0:
        return False
    elif a+b<c or a+c<b or b+c<a:
        return False
    elif a+b==c or a+c==b or b+c==a:
        return False
    return True


def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))