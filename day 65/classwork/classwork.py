def remove(st):
    return st.rstrip("!")


def list_animals(animals):
    lst = ''
    for i in range(animals):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst


def integrate(coe, exp):
    x=exp+1
    return f"{coe//x}x^{x}"


def break_chocolate(n, m):
    if n*m==0:
        return 0
    
    return n*m-1

def is_anagram(test, org):
    x=test.lower()
    y=org.lower()
    return sorted(x)==sorted(y)

def in_asc_order(arr):
    return arr==sorted(arr)

