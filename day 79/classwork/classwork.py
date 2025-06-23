def small_enough(arr, limit):
    x=sorted(arr)
    return x[-1]<=limit

def largest_pair_sum(num): 
    x=sorted(num)
    return x[-1]+x[-2]

def spin_words(sentence):
    list=sentence.split()
    result=[]
    for i in list:
        if len(i)>=5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)

def delete_nth(order,max):
    res = []
    for i in order:
        if res.count(i)<max:
            res.append(i)
            
    return res

