def solution(string):
    return string[::-1]


def sum_array(a):
    return sum(a)


def unique_in_order(iterable):
    x= []
    for i in iterable:
        if x == []:
            x.append(i)
        elif x[-1] != i:
            x.append(i)
    return x

