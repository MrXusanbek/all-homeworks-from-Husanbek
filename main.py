# 4 -oy 8_dars amaliyot
# 1 misol
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)
#--------------------------------------------
# 2 misol
# letters = ["A", "a", "B", "b", "C", "c", "D", "d"]
# uppercase_letters = list(filter(str.isupper, letters))
# print(uppercase_letters)
#--------------------------------------------
# 3 misol
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# countries = list(map(lambda x: x[:4], phone_numbers))
# print(countries)
#--------------------------------------------
# 4 misol
# names = ['alfred', 'tabitha', 'william', 'arla']
# def capitalize_name(name):
#     return name.capitalize()
#
# capitalized_names = list(map(capitalize_name, names))
# print(capitalized_names)
#--------------------------------------------
# 5 misol
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def greater_than_75(score):
#     return score > 75
#
# high_scores = list(filter(greater_than_75, scores))
# print(high_scores)
#--------------------------------------------
# 6 misol
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# palindromes = list(filter(lambda word: word.lower() == word[::-1].lower(), words))
# print(palindromes)
#---------------------------------------------
# 7 misol
# words = ['apple', 'banana', 'cherry']
# lengths = list(map(len, words))
# print(lengths)
#-------------------------------------
# 8 misol
# list1 = ['apple', 'banana', 'cherry']
# list2 = ['orange', 'lemon', 'pineapple']
# combined = list(map(lambda x, y: x + y, list1, list2))
# print(combined)
#-----------------------------------------------
# 9 misol
# list1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# list2 = ["Sobir", "Bakir", "Jalil", "Toxir"]
# combined = list1 + list2
# print(combined)
#----------------------------------------
# 10 misol
# def count_occurrences(lst, elem):
#     return lst.count(elem)
#
# my_list = [1, 2, 3, 2, 4, 2, 5]
# element = 2
# print(count_occurrences(my_list, element))
#---------------------------------------
# 11 misol
# list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common_elements = list(set(list1) & set(list2))
# print(common_elements)
#-----------------------------------------
# 12 misol
# languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# odd_index_elements = languages[::2]
# print(odd_index_elements)
# #-------------------------------------------
# # 13 misol
# languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# start_index = languages.index("Basic")
print(languages[start_index:])
#---------------------------------------------
# 14 misol
# from collections import namedtuple
#
# Student = namedtuple('Student', ['name', 'group', 'average'])
# students = [
#     Student('Ali', 'A1', 89),
#     Student('Vali', 'A2', 76),
#     Student('Karim', 'A1', 94),
#     Student('Said', 'A3', 67),
#     Student('Nodir', 'A2', 88),
# ]
#
# top_student = max(students, key=lambda s: s.average)
# print(top_student)
#------------------------------------------------------
# 15 misol
# def square_generator():
#     for i in range(1, 21):
#         yield i ** 2
#
# for square in square_generator():
#     print(square, end=" ")
#------------------------------------------
# 16 misol
# def text_length_closure():
#     def length(text):
#         return len(text)
#     return length
#
# get_length = text_length_closure()
# print(get_length("Salom!"))
#-------------------------------------------
# 17 misol
# def greeting_closure():
#     def greet(name):
#         return f"Salom, {name}!"
#     return greet
#
# greet = greeting_closure()
# print(greet("Husanbek"))
#---------------------------------------------------------------------------