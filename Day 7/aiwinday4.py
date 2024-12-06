def find_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = find_even_numbers(input_list)
print(result)