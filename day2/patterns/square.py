b=5
l=5
for i in range (l):
    for j in range (b):
        if i==0 or i==l-1 :
            print('*', end="")
        elif j==0 or j==b-1:
            print('*', end="")
        else:
            print(' ', end="")
    print('')

