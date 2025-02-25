# 2nd highest number in a list

def scndLargest(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second

list = [8,8,7,7, 5, 10, -3, 2, 7,1,9]
print(scndLargest(list)) 