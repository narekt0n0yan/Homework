# import os

# # Base directory and filename
# base_dir = r'/C:\Users\narek'
# filename = r'\Рабочий стол\boocsv'

# # Construct the full path
# full_path = os.path.join(base_dir, filename)

# # Reading and writing files using the full path

# print(full_path)





import numpy as np

# Create an empty array with the specified shape
shape = (3, 4)  # For example, a 3x4 array
empty_array = np.empty(shape)

print(empty_array[0][0])
print(type(empty_array[0][0]))


# print('=====================================================')


# empty_array = np.empty(shape, dtype=int)

# print(empty_array)
