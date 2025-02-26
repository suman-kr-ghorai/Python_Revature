# users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,
# # "Chicago")]
# You are given a list of tuples containing user data in the format (name, age, city) .
# Create a dictionary comprehension that maps each user's name to their age, but only
# include users who are older than 18.

users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,"Chicago")]
dict={name:age  for name,age,city in users if age>18}
print(dict)
