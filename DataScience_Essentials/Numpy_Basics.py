import numpy as  np
# Creating and Manipulating arrays
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2]) #array indexing
print(arr[-1])

print(arr[1:4]) # array slicing
print(arr[3:])

reshaped = arr.reshape(2,3) # array reshaping
print("Reshaped: ",reshaped)

expanded= arr[:,np.newaxis]
print("Expanded: ",expanded)

a = np.arange(1, 6)
b = np.arange(6,11)


print(a)
print(b)

print("Add: ", a + b)
print("Sub: ", a - b)
print("Mult: ", a * b)
print("Div: ", a / b)
print("Sqrt: ", np.sqrt(arr))
print("Mean: ",np.mean(arr))
print("Max: ",np.max(arr))
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix: \n", matrix)

# Transpose
transpose = matrix.T
print("Transpose:\n", transpose)

another_matrix = np.array([[9,8,7], [6,5,4], [3,2,1]])
print("Addition: \n", matrix + another_matrix)
print("Multiplication : \n", matrix * another_matrix)

# Column & Row wise sum
print("Column Sum: ",np.sum(matrix,axis=0))
print("Row Sum: ",np.sum(matrix,axis=1))

# normalization
mat_min= matrix.min()
mat_max=matrix.max()
normalized= (matrix-mat_min)/(mat_max-mat_min)
print("Normalized: ", normalized)