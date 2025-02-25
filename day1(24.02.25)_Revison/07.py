# lst=[1,22,2,5,2,7]

# def removeDuplicates(lst):
#     return list(set(lst))
# def removeDuplicates2(lst):
#     pass

# print(removeDuplicates(lst))

# def returnDuplicates(lst):
#     return [item for item in lst if lst.count(item)>1],list(set(lst))
# print(returnDuplicates(lst))


# def returnSeen(lst):
#     seen=set()
#     distinct=[]
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             distinct.append(item)
#     return seen,distinct
# print(returnSeen(lst))


# def returnSeen(lst):
#     seen = set()
#     duplicates = set()
#     distinct = []
    
#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#             distinct.append(item)
#     return  distinct, duplicates

def returnSet(lst):
    seen=set()
    distinct=[]

    for item in lst:
        if item not in seen:
            distinct.append(item)
        else:
            seen.add(item)
    return distinct, seen

lst = [1, 2, 3, 4, 2, 3, 5, 6, 6]
print(returnSet(lst)) 
