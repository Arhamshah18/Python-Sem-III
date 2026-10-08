import numpy as np

# 1. Create a 1D array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Slicing operations (Extract elements from index 2 to 6)
sliced_arr = arr[2:7]
print("Sliced Array (index 2 to 6):", sliced_arr)

# 3. Statistical measures
print(f"Sum: {np.sum(arr)}")
print(f"Mean: {np.mean(arr):.2f}")
print(f"Max: {np.max(arr)}")
print(f"Min: {np.min(arr)}")

# 4. Broadcasting (Multiply all elements by 10)
broadcasted_arr = arr * 10
print("Array after Broadcasting (* 10):", broadcasted_arr)
