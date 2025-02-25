def scndLargest(lst):
    return (set(lst.sort()))[-2]
    # return lst[-2]
list = [8,8,7,7, 5, 10, -3, 2, 7,1]
print(scndLargest(list)) # 8