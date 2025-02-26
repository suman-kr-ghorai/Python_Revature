# transpose matrix
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# output=[[1,4,7],[2,5,8],[3,6,9]]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output1=[[matrix[j][i] for j in range(3)] for i in range(3)]
print(output1)