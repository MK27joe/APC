#### Ref: https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-141.php

import numpy as np
import pandas as pd


# Creating a NumPy array 'arra_data' containing integers from 0 to 15 and reshaping it into a 4x4 matrix
arra_data = np.arange(0, 16).reshape((4, 4))

# Displaying a message indicating the original array will be printed
print("Original array:")

# Printing the original 4x4 array 'arra_data'
print(arra_data)

# Displaying a message indicating the extracted data (all the elements of the second and third columns)
print("\nExtracted data: All the elements of the second and third columns")

# Using slicing to extract all rows and specific columns (2nd and 3rd columns) from 'arra_data'
print(arra_data[:, [1, 2]])

print("\nExtracted data: All the elements of rows 1 and 2")
print(arra_data[:2, :])

print("\nExtracted data: All the elements of rows 3 and 4")
print(arra_data[[2, 3], :])

