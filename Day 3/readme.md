Day 3: If, Elif and Else Function #1
## **Task**: Write a Python program that takes a number as input from the user and checks if the number is:
1. Positive
2. Negative
3. Zero.

**Description**:
if: Checks a condition and runs the code if it's True.
elif: Checks another condition if the if is False.
else: Runs code if none of the if or elif conditions are True.

**Example**:
```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
