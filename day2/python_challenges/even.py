# even=[i%2==0 for i in range(1,11)]
# print(even)
l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print (l)


even = [i for i in range(1, 11) if i % 2 == 0]
print(even)
