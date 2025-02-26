string = "Hello, World!"
unique_in_order1=[]
unique_in_order=[unique_in_order1.append(char.lower()) for char in string if char.isalpha() and char.lower() not in unique_in_order1]
print(unique_in_order1)