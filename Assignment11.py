import pandas as pd
import numpy as np

# 1. Create a Series with 10 random numbers
np.random.seed(42)  # For reproducible results
series = pd.Series(np.random.randint(1, 100, size=10), name="Random_Numbers")
print("Pandas Series:\n", series, "\n")

# 2. Indexing (Access element at index 3)
print("Element at index 3:", series[3])

# 3. Filtering (Elements strictly greater than 50)
filtered_series = series[series > 50]
print("\nFiltered Series (Values > 50):\n", filtered_series)

# 4. Statistical measures
print("\nStatistical Measures:")
print(f"Mean:   {series.mean():.2f}")
print(f"Median: {series.median():.2f}")
print(f"Min:    {series.min()}")
print(f"Max:    {series.max()}")
