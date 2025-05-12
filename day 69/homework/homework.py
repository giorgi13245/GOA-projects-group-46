def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


def find_it(seq):
    for i in seq:
        if seq.count(i)%2==1:
            return i
        


def array_diff(a, b):
    return [i for i in a if i not in b]

def is_palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False
    

