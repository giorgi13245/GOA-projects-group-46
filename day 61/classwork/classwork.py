def get_average(marks):
    return sum(marks) // len(marks)


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


def number(bus):
    sum=0
    for i in bus:
        sum+=i[0]-i[1]
    return sum



def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def find_it(seq):
    for i in seq:
        if seq.count(i)%2==1:
            return i