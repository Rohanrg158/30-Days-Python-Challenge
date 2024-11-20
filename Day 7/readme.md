Day 7: Lists
## **Task**: Write a Python function find_even_numbers that takes a list of integers as input and returns a new list containing only the even numbers from the input list.

**Description**:
A list in Python is an ordered, mutable collection of elements that can store multiple items, such as numbers, strings, or other objects, allowing for indexing, slicing, and modification.

**Example**:
```python
def find_even_numbers(input_list):
    # Use a list comprehension to filter out the even numbers
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = find_even_numbers(input_list)
print(result)

Output: 
[2, 4, 6, 8]
