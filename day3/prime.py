def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True



prime={i for i in range(1,51) if prime(i)} 
print(prime)
