print "Hello World"

print('Hello, GitHub!')

#laba 2 funkcii
print("Таблица умножения:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="\t")
    print()

sum_odd = 0
for i in range(1, 101, 2):
    sum_odd += i
print("\nСумма нечётных чисел от 1 до 100:", sum_odd)

n = int(input("\nВведите число для поиска делителей: "))
print(f"Делители числа {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

n = int(input("\nВведите число для вычисления факториала: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n}: {factorial}")

n = int(input("\nВведите длину последовательности Фибоначчи: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print("Последовательность Фибоначчи:", fib[:n])

#blok2
import random

numbers = [random.randint(-5, 5) for z in range(10)]
print("Исходный список:", numbers)

print("\nЧётные элементы:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("\nМаксимальное число:", max_num)
print("Минимальное число:", min_num)

user_numbers = []
for i in range(5):
    num = int(input("\nВведите число: "))
    user_numbers.append(num)
user_numbers.sort()
print("Отсортированный список:", user_numbers)

print("Задание 4:")
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("\nСписок без дубликатов:", unique_numbers)

print("Задание 5:")
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("\nСписок после обмена первого и последнего элементов:", numbers)

#blok3
students = {
    "Маша": 12,
    "Дарья": 45,
    "Богдан": 19,
    "Анна": 14,
    "Софья": 32,
    "Наталья": 34
}
average_score = sum(students.values()) / len(students)
print("Оценки студентов:", students)
print("Средний балл:", average_score)

text = input("\nВведите строку: ")
letter_count = {}
for buk in text:
    if buk.isalpha():  # Учитываем только буквы
        letter_count[buk] = letter_count.get(buk, 0) + 1 #есть ли, возв знач, ищет значения
print("Количество каждой буквы:", letter_count)

squares = {i: i**2 for i in range(1, 11)}
print("\nЧисла и их квадраты:", squares)

keys = ["Имя", "Возраст", "Город"]
values = ["Даша", 34, "Аксай"]
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print("\nСловарь из двух списков:", combined_dict)

#blok4
set1 = {1, 2, 3, 4, 5, 6, 9} #неупорядоченная коллекция уникальных элементов.
set2 = {4, 5, 6, 7, 8, 12, 9}
print("Множество 1:", set1)
print("Множество 2:", set2)
print("Пересечение:", set1.intersection(set2))
print("Объединение:", set1.union(set2))

text = input("\nВведите текст: ")
words = text.lower().split()
word_counts = {word: words.count(word) for word in set(words)}  #подсчёт вхождений слов
unique_words = [word for word in words if word_counts[word] == 1]  #слова, встречающиеся один раз
print("Уникальные слова (встречаются один раз):", unique_words)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2) #пересечение
print("\nСписок 1:", list1)
print("Список 2:", list2)
print("Общие элементы:", common_elements)

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print("\nМножество A:", set_a)
print("Множество B:", set_b)
print("A является подмножеством B:", set_a.issubset(set_b))

numbers = {1, 3, 5, 7, 9, 2, 4, 6, 8}
b = int(input("\nВведите число для удаления элементов меньше него: "))
numbers.difference_update({x for x in numbers if x < b})#удаляет из множества
# numbers все элементы, которые присутствуют в переданном множестве
print("Множество после удаления:", numbers)

#blok5
import random

numbers = [random.randint(1, 51) for b in range(20)]
unique_numbers = list(set(numbers))
print("Список чисел:", numbers)
print("Уникальные значения:", unique_numbers)

vstr_dict = {}
for item in numbers:
    vstr_dict[item] = vstr_dict.get(item, 0) + 1
print(f"Словарь частот: {vstr_dict}\n")

words = ["яблоко", "груша", "апельсин", "банан", "ананас", "виноград", "киви"]
long_words = {word for word in words if len(word) > 5}
print("\nСлова:", words)
print("Множество слов длиннее 5 символов:", long_words)

sentence = input("\nВведите предложение: ")
word_counts = {word: sentence.lower().split().count(word) for word in set(sentence.lower().split())}
#перебирает уникальные слова из множества
print("Количество вхождений слов:", word_counts)

number_list = [1, 2, 2, 3, 4, 4, 5]
number_set = set(number_list)
unique_list = list(number_set)
print("\nИсходный список:", number_list)
print("Множество:", number_set)
print("Список без дубликатов:", unique_list)

products = {"яблоко": 50, "банан": 50, "апельсин": 70, "груша": 60, "мясо": 500}
most_expensive = max(products, key=products.get)
print(f"Словарь товаров: {products}")
print(f"Самый дорогой товар: {most_expensive} (цена: {products[most_expensive]})\n")

names = ["Алексей", "Мария", "Иван", "Алексей", "Мария", "Мария", "Дарья", "Софья"]
name_counts = {name: names.count(name) for name in set(names)}
repeated_names = {name: count for name, count in name_counts.items() if count > 1}
most_common_name = max(name_counts, key=name_counts.get)
count = max(name_counts.values())
print("\nИмена:", names)
print("Имена, встречающиеся более одного раза:", repeated_names)
print("Самое частое имя:", most_common_name, "(встречается", count, "раз)")

text = input("\nВведите строку: ")
char_indices = {char: text.index(char) for char in text}
print("Словарь символов и их первых вхождений:", char_indices)
