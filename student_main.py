def task1(a, b, c):
    max_number = max(a, b, c)
    return max_number

# Example usage:
result = task1(5, 12, 8)
print(result)  # This will print the maximum of 5, 12, and 8

def task2(numbers):
    sum_result = sum(numbers)
    return sum_result

# Example usage:
sample_list = [8, 2, 3, 0, 7]
result = task2(sample_list)
print(result)  # This will print the sum of the numbers in the sample list

def task3(numbers):
    product_result = 1  # Initialize the product to 1
    for num in numbers:
        product_result *= num
    return product_result

# Example usage:
sample_list = [8, 2, 3, -1, 7]
result = task3(sample_list)
print(result)  # This will print the product of the numbers in the sample list

def task4(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage:
sample_string = "1234abcd"
result = task4(sample_string)
print(result)  # This will print the reversed string of "1234abcd"

def task5(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial_result = 1
        for i in range(2, n + 1):
            factorial_result *= i
        return factorial_result

# Example usage:
sample_integer = 3
result = task5(sample_integer)
print(result)  # This will print the factorial of 3

def task6(number):
    return 25 <= number <= 50

# Example usage:
sample_integer = 512
result = task6(sample_integer)
print(result)  # This will print False as 512 is outside the range (25-50)

def task7(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
sample_string = 'The quick Brow Fox'
result = task7(sample_string)
print(result)  # This will print (3, 12) indicating 3 uppercase letters and 12 lowercase letters

def task8(input_list):
    distinct_list = list(set(input_list))
    return distinct_list

# Example usage:
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result = task8(sample_list)
print(result)  # This will print [1, 2, 3, 4, 5] - a list with distinct elements

def task9(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Example usage:
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = task9(sample_list)
print(result)  # This will print [2, 4, 6, 8] - a list containing only even numbers

def task10(row_index):
    def generate_pascals_triangle(n):
        triangle = [[1] * (i + 1) for i in range(n)]
        for i in range(2, n):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle

    pascals_triangle = generate_pascals_triangle(row_index + 1)
    last_row = pascals_triangle[-1]
    max_number = max(last_row)
    return max_number

# Example usage:
row_index = 5
result = task10(row_index)
print(result)  # This will print the max number in the last row of Pascal's triangle with index 5

