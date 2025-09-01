def filter_list(l):
    res=[]
    for i in l:
        if type(i)==int:
            res.append(i)
            
    return res


def delete_nth(order,max):
    res = []
    for i in order:
        if res.count(i)<max:
            res.append(i)
            
    return res

