def update_light(current):
    dict={
        "green":"yellow",
        "yellow":"red",
        "red":"green"
    }
    
    return dict[current]


def count_by(x, n):
    list=[]
    for i in range(x,x*n+1,x):
        list.append(i)
    return list


def abbrevName(name):
    x=[]
    a = name.split(" ")
    for i in a:
        x.append(i[0].upper())
    return ".".join(x)

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

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"