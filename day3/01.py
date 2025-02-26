# # Question 1: List Comprehension - Random DNA Helix
# Pattern
# Write a Python program that generates a random DNA sequence of length 20 using the
# characters A , T , C , and G . Use a list comprehension to create the sequence.

import random 


# DNA sequence
dna = ['A', 'T', 'C', 'G']

DNALIST=[random.choice(dna) for i in range (20)]
print(DNALIST)