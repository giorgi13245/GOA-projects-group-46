def likes(names):
    if not names or names==[] or len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return f"{names[0]} likes this"
    elif len(names)==2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names)==3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names)>3:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


def find_it(seq):
    for i in seq:
        if seq.count(i)%2==1:
            return i
        

def row_weights(arr):
    res=[]
    res1=[]
    
    for i in range(len(arr)):
        if (i+1)%2==1:
            res.append(arr[i])
        else:
            res1.append(arr[i])
            
    return (sum(res), sum(res1))

def largest_pair_sum(num): 
    x=sorted(num)
    return x[-1]+x[-2]