def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += x
    return [pos, neg]


def are_you_playing_banjo(name):

    
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    

def simple_multiplication(number) :
    if number%2==0:
        return number * 8
    else:
        return number * 9
    

def invert(lst):
    result=[]
    for i in lst:
        result.append(-i)
    return result

def grow(arr):
    result=1

    for i in arr:
        result *=i

    return result


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])