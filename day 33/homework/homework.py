#1
def double_integer(i):
    return i*2

#2
def friend(x):
    
    result=[]

    for i in x:
        if len(i)==4:
            result.append(i)

    return result


#3
def grow(arr):
    result=1

    for i in arr:
        result *=i

    return result


#4
def find_average(numbers):
    if not numbers:  
        return 0
    return sum(numbers) / len(numbers)


#5
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague

#6
def double_char(s):
    result=""

    for i in s:
        result +=1*2

    return result

#7
def remove_url_anchor(url):
    index=url.find("#")
    if index>-1:
        return url[:index]
    else:
        return url
    


#8
def sum_cubes(n):
    result=0

    for i in range(1, n+1):
        result+= 1**3

    return result




nums=[1,2,4,7,3]
nums.pop(3)
nums.insert(0,30)
print(nums)


def function(num1,num2):
    return num1**num2

print(function(2,3))


def lists(list):
    if len(list)%2==0:
        return "List length is even"
    else:
        return "List length is odd"


