import numpy as np
import os

data = np.load('data.npz')

if not os.path.exists("cpp_data"):
    os.makedirs("cpp_data")

    
for key in data.files:
    arr = data[key]
    file_path = f"cpp_data/{key}.bin"
    arr.tofile(file_path)
