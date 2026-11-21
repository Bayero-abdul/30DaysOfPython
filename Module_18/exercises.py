"""Solutions for the NumPy and Pandas exercises in Module 18."""

from pathlib import Path

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# NumPy exercises: repeat the main examples
# ---------------------------------------------------------------------------

print("=== NumPy ===")
print("NumPy version:", np.__version__)

python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)
print("Array:", numpy_array)
print("Array shape:", numpy_array.shape)
print("Array size:", numpy_array.size)
print("Array dtype:", numpy_array.dtype)

print("Array + 10:", numpy_array + 10)
print("Array * 10:", numpy_array * 10)
print("Array ** 2:", numpy_array**2)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", matrix)
print("First row:", matrix[0])
print("First column:", matrix[:, 0])
print("Top-left 2x2 slice:\n", matrix[0:2, 0:2])
print("Reversed matrix:\n", matrix[::-1, ::-1])

reshaped = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)
print("Reshaped array:\n", reshaped)
print("Flattened array:", reshaped.flatten())
print("Horizontal stack:", np.hstack(([1, 2, 3], [4, 5, 6])))
print("Vertical stack:\n", np.vstack(([1, 2, 3], [4, 5, 6])))

print("Arange:", np.arange(1, 20, 2))
print("Linspace:", np.linspace(1.0, 5.0, num=10))
print("Random normal sample shape:", np.random.normal(79, 15, 80).shape)

print("Matrix minimum:", matrix.min())
print("Matrix maximum:", matrix.max())
print("Matrix mean:", matrix.mean())
print("Matrix median:", np.median(matrix))
print("Matrix standard deviation:", matrix.std())
print("Column minimums:", np.amin(matrix, axis=0))
print("Row maximums:", np.amax(matrix, axis=1))

values = np.array([1, 2, 3])
print("Tile:", np.tile(values, 2))
print("Repeat:", np.repeat(values, 2))

# ---------------------------------------------------------------------------
# Pandas exercises
# ---------------------------------------------------------------------------

print("\n=== Pandas ===")

csv_path = (
    Path("/home/abdulbayero/Projects/30-Days-of-Python-main/data/hacker_news.csv")
)
if not csv_path.exists():
    raise FileNotFoundError(f"Could not find the Hacker News CSV at {csv_path}")

df = pd.read_csv(csv_path)

# 1. Read the CSV file.
print("CSV loaded:", df.shape)

# 2. Get the first five rows.
print("\nFirst five rows:")
print(df.head())

# 3. Get the last five rows.
print("\nLast five rows:")
print(df.tail())

# 4. Get the title column as a Pandas Series.
titles = df["title"]
print("\nTitle Series:")
print(titles.head())

# 5. Count the number of rows and columns.
rows, columns = df.shape
print("\nRow and column count:", rows, columns)

# Filter titles containing Python (case-insensitive).
python_titles = df[df["title"].str.contains("python", case=False, na=False)]
print("\nTitles containing 'python':", len(python_titles))
print(python_titles[["title"]].head(10).to_string(index=False))

# Filter titles containing JavaScript (case-insensitive).
javascript_titles = df[df["title"].str.contains("javascript", case=False, na=False)]
print("\nTitles containing 'JavaScript':", len(javascript_titles))
print(javascript_titles[["title"]].head(10).to_string(index=False))

# Additional exploration to make sense of the data.
print("\nDataset columns:", list(df.columns))
print("Missing values by column:")
print(df.isna().sum())
print("Highest-scoring story:")
print(df.loc[df["num_points"].idxmax(), ["title", "num_points", "num_comments"]])
print("Most-discussed story:")
print(df.loc[df["num_comments"].idxmax(), ["title", "num_points", "num_comments"]])
