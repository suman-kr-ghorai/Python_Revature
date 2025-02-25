names=["John", "Jack", "Jill", "Jenny", "Jasmine"]

result=[(name,len(name)) for name in names]
print(result)

result1=[(x,y) for x in [1,2,3] for y in [4,5,6] if x!=y] 
print(result1)