Day 4: For Loop
## **Task**: Write a Python program that takes a list of numbers and prints only the even numbers from the list.

**Description**:
A for loop in Python is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code multiple times, once for each item in the sequence.

**Example**:
```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list and print even numbers
for num in numbers:
    if num % 2 == 0:
        print(num)
Output:
2
4
6
8
10
