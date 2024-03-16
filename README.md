# Homework
This repository is only for uploading homework.

# Greatest subset
## Description
This Python script is designed to identify the greatest non-negative subset from a randomly generated list of integers. It iterates through the list, extracting subsets of non-negative integers and comparing them to find the subset with the largest sum.

## How it works
1. The script generates a list `mainset` containing 100 random integers between -100 and 100.
2. It initializes several lists and variables to keep track of subsets and their sums.
3. It iterates through each element of `mainset`, adding non-negative integers to `lastsubset`.
4. When encountering a negative integer, it checks if there's more than one negative integer in a row.
5. If the current `lastsubset` has a greater sum than the previously identified greatest subset, it updates `greatestsubset`.
6. Finally, it prints the `greatestsubset` and the sum of its elements.

## Usage
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., `greatest_subset.py`).
3. Run the script using a Python interpreter.
4. View the output to see the greatest non-negative subset and the sum of its elements.

## Example Output
~~~Python
[-54, -17, 57, -63, 22, 86, -15, 81, -97, 33, -33, 35, -92, -25, -12, 6, -20, -9, 58, -52, 57, -77, -81, -41, -93, -32, -87, -35, 28, -16, 33, 8, -69, -58, -31, -58, -26, -35, -51, 27, 72, 77, -5, -24, 29, -12, 14, -92, -80, -77, -12, -24, 22, -2, 58, 33, -48, -58, -20, 3, -2, 52, 44, -68, -95, 64, 12, 20, 80, -5, 68, -17, 28, 32, 59, 6, 37, -82, 66, 52, 56, -15, 14, -74, -36, -53, -3, 13, -41, 59, -49, 100, 66, -87, 92, -6, -99, -46, 23, -31]
[27, 72, 77]
176
~~~
## Dependencies
- Python 3.x
- `random` module (built-in)

## Author
This script was written by Murguia Ortiz Joaquin de Jesus.
