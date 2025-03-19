def get_volume_of_cuboid(len, wid, hei):
    return len*wid*hei


def find_average(nums):
    return sum(nums)/len(nums)


def no_boring_zeros(n):
    if n==0:
        return n
    while n%10==0:
        n=n/10
    return n


def final_grade(exam, proj):
    if exam>90 or proj>10:
        return 100
    elif exam>75 and proj>=5:
        return 90
    elif exam>50 and proj>=2:
        return 75
    else:
        return 0
    


def maps(a):
    result=[]
    for i in a:
        result.append(i*2)
    return result


def hero(bullets, dragons):
    if bullets/2>dragons or bullets/2==dragons:
        return True
    else:
        return False