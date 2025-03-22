def distinct(seq):
    x=[]
    for i in seq:
        if i not in x:
            x.append(i)
    return x


def get_planet_name(id):
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name


def switch_it_up(num):
    dict={
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
    }
    
    return dict[num]


def unusual_five():
    x=["a","b","c","d","e"]
    return len(x)