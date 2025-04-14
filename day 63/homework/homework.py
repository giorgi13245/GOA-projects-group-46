def is_isogram(str):
    a=str.lower()
    return len(a)==len(set(a))


def to_jaden_case(string):
    list=string.split()
    list2=[]
    for i in list:
        i=i.capitalize()
        list2.append(i)
    return " ".join(list2)


def validate_pin(pin):
    if len(pin)==4 and pin.isnumeric()==True:
        return True
    elif len(pin)==6 and pin.isnumeric()==True:
        return True
    else:
        return False
    

def row_sum_odd_numbers(n):
    return n**3


