# Lab.4
Функція task1

def task1(a, b, c):
    max_number = max(a, b, c)  # Знаходить найбільше число серед трьох вхідних параметрів
    return max_number  # Повертає найбільше число
Опис:

Вхідні параметри: a, b, c - цілі числа.
Знаходить найбільше число серед a, b, c за допомогою вбудованої функції max().
Повертає знайдене найбільше число.
Функція task2

def task2(numbers):
    sum_result = sum(numbers)  # Обчислює суму всіх елементів у вхідному списку numbers
    return sum_result  # Повертає суму всіх елементів у вхідному списку
Опис:

Вхідний параметр: numbers - список цілих чисел.
Обчислює суму всіх чисел у списку numbers за допомогою вбудованої функції sum().
Повертає знайдену суму.
Функція task3

def task3(numbers):
    product_result = 1  # Ініціалізує добуток до 1
    for num in numbers:
        product_result *= num  # Обчислює добуток всіх елементів у вхідному списку numbers
    return product_result  # Повертає добуток всіх елементів у вхідному списку
Опис:

Вхідний параметр: numbers - список цілих чисел.
Ініціалізує змінну product_result до 1 (так як добуток числа на 1 дорівнює самому числу).
Проходиться по кожному числу num у списку numbers і множить його до поточного значення product_result.
Повертає отриманий добуток всіх елементів у вхідному списку.
Функція task4

def task4(input_string):
    reversed_string = input_string[::-1]  # Обертає вхідний рядок за допомогою зрізу
    return reversed_string  # Повертає обернутий рядок
Опис:

Вхідний параметр: input_string - рядок символів.
Використовує зріз [::1], що обертає рядок input_string.
Повертає обернутий рядок.
Функція task5

def task5(n):
    if n == 0 or n == 1:
        return 1  # Повертає 1, якщо n дорівнює 0 або 1 (факторіал 0 та 1 дорівнює 1)
    else:
        factorial_result = 1  # Ініціалізує результат факторіала до 1
        for i in range(2, n + 1):
            factorial_result *= i  # Обчислює факторіал числа n
        return factorial_result  # Повертає обчислений факторіал числа n
Опис:

Вхідний параметр: n - ціле число.
Перевіряє, чи n дорівнює 0 або 1. Якщо так, повертає 1 (факторіал 0 і 1 дорівнює 1).
Якщо n більше 1, ініціалізує змінну factorial_result до 1 і обчислює факторіал числа n за допомогою циклу for.
Повертає обчислений факторіал числа n.
Функція task6

def task6(number):
    return 25 <= number <= 50  # Повертає True, якщо number знаходиться у діапазоні від 25 до 50, включно
Опис:

Вхідний параметр: number - ціле число.
Повертає True, якщо number знаходиться у діапазоні від 25 до 50 (включно), інакше повертає False.
Функція task7

def task7(input_string):
    upper_count = 0  # Лічильник великих літер
    lower_count = 0  # Лічильник малих літер

    for char in input_string:
        if char.isupper():
            upper_count += 1  # Лічить кількість великих літер
        elif char.islower():
            lower_count += 1  # Лічить кількість малих літер

    return upper_count, lower_count  # Повертає кортеж із кількістю великих і малих літер у вхідному рядку
Опис:

Вхідний параметр: input_string - рядок символів.
Ініціалізує два лічильники: upper_count і lower_count.
Проходиться по кожному символу char у вхідному рядку input_string.
Якщо char є великою літерою (за допомогою char.isupper()), збільшує upper_count.
Якщо char є малою літерою (за допомогою char.islower()), збільшує lower_count.
Повертає кортеж із кількістю великих і малих літер у вхідному рядку.
Функція task8

def task8(input_list):
    distinct_list = list(set(input_list))  # Видаляє дублікати зі списку input_list і перетворює його у список
    return distinct_list  # Повертає список із унікальними елементами
Опис:

Вхідний параметр: input_list - список елементів.
Використовує set(input_list), що видаляє дублікати у списку input_list.
Перетворює отримане множину назад у список distinct_list.
Повертає список із унікальними елементами.
Функція task9

def task9(input_list):
    even_numbers = [num for num in input_list if num % 2 =
