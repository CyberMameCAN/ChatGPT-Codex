
"""Sample scripts demonstrating various for loop patterns in Python."""


def basic_for_loop():
    """Basic for loop over a list."""
    numbers = [1, 2, 3]
    for n in numbers:
        print(n)


def enumerate_loop():
    """For loop using enumerate to track indices."""
    fruits = ["apple", "banana", "cherry"]
    for idx, fruit in enumerate(fruits, start=1):
        print(idx, fruit)


def dataframe_loops():
    """Demonstrate common ways to iterate over a DataFrame."""
    import pandas as pd

    data = {
        "A": [1, 2, 3],
        "B": ["x", "y", "z"],
        "C": [10, 20, 30],
    }
    df = pd.DataFrame(data)

    print("\n-- items --")
    for col, series in df.items():
        print(col, series.tolist())

    print("\n-- iterrows --")
    for index, row in df.iterrows():
        print(index, row["A"], row["B"], row["C"])

    print("\n-- itertuples --")
    for row in df.itertuples(index=False):
        print(row.A, row.B, row.C)

    print("\n-- groupby('B') --")
    for key, group in df.groupby("B"):
        print(key)
        print(group)


if __name__ == "__main__":
    print("basic_for_loop")
    basic_for_loop()

    print("\nenumerate_loop")
    enumerate_loop()

    print("\ndataframe_loops")
    dataframe_loops()
