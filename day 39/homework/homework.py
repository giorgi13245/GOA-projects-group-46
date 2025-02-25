def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    else:
        return "No"
    



def repeat_str(repeat, string):
    return string*repeat



def century(year):
    if year%100==0:
        return year//100
    else:
        return year//100+1
    

def find_smallest_int(arr):
    return min(arr)


def hero(bullets, dragons):
    if bullets/2>dragons or bullets/2==dragons:
        return True
    else:
        return False