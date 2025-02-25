def nth_even(n):
    return 2 * (n - 1)



def add_length(str_):
    answer = []
    for i in str_.split():
        answer.append(i + ' ' + str(len(i)))
    return answer


def array(string):
    return " ".join(string.split(",")[1:-1]) or None


def find_difference(a, b):
    a1=a[0]*a[1]*a[2]
    b1=b[0]*b[1]*b[2]
    return abs(a1-b1)