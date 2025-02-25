# print("Hello")
def closestToZero(numbers):
    return min(numbers,key=lambda x:abs(x),)
list = [8, 5, 10, -3, 2, 7,1]
print(closestToZero(list)) # 1