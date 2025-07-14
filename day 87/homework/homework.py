def between(a,b):
    return [i for i in range(a,b+1)]

def correct(s):
    s=s.replace("0", "O")
    s=s.replace("5", "S")
    s=s.replace("1", "I")
    return s

def str_count(strng, letter):
    return strng.count(letter)

def string_to_array(s):
    if s=="":
        return [""]
    return s.split()

def digitize(n):
    return [int(i) for i in str(n)][::-1]

def sum_cubes(n):
    return sum([i**3 for i in range(1,n+1)])

def to_float_array(arr):
    res=[]
    for i in arr:
        if "." in i:
            res.append(float(i))
        else:
            res.append(int(i))
            
    return res