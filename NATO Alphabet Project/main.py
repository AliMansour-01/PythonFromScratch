number = [1, 2, 3]
new_numbers = [item + 1 for item in number]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)


range_list = [num + num for num in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)