import numpy as np

#BroadCasting #allows numpy to perform arithmetic ops on arrays of different shapes
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0 , -1])

result_add = matrix + vector #1D broadCasting
print("Add: \n", result_add)

result_mul = matrix * 2 #scalar broadCasting
print("Multiplication: \n", result_mul)

#Random Generator
np.random.seed(42)

random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array) # generate a random array of size 3X3


random_integers = np.random.randint(0, 10, size=(2,3)) # generate a random array of size 2X3 withintegers ranging from 0-10
print("Random Integers: \n", random_integers)

#Example 1:

# Generate random dataset
dataset = np.random.randint(1, 51, size=(5,5))
print("Original: \n", dataset)

# Filter values > 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified Dataset: \n", dataset)


# calculate summary stats --Aggregate Functions
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))