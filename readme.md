Day 6: Continue Statement
## **Task**: Write a Python program that prints all even numbers from 1 to 20, but skips the number 12.

Use a for loop to iterate through the numbers from 1 to 20.
Use the continue statement to skip the number 12.
Print each even number, except for 12.

**Description**:
The continue statement is another control flow tool used within loops. It skips the current iteration and moves to the next iteration of the loop. This is useful when you want to skip certain parts of the loop based on a condition.
**Example**:
```python
for i in range(1, 21):  # Loop through numbers from 1 to 20
    if i == 12:
        continue  # Skip the number 12
    if i % 2 == 0:  # Check if the number is even
        print(i)  # Print the even number

Output: 
2
4
6
8
10
14
16
18
20
