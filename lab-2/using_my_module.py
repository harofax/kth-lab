print("----------- IMPORT ---------------\n")

import my_module
import math


# Uppgift 1 (givet)
print("\n----------- UPG 1 ---------------\n")

y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))


# Uppgift 2 (att skrivas)
print("\n----------- UPG 2 ---------------\n")

print("x = 5:\t\t",my_module.my_function(5))
print("x = pi/2:\t", my_module.my_function(math.pi/2))


# Uppgift 3 (att skrivas)
print("\n----------- UPG 3 ---------------\n")

print("sum 5 dice:", my_module.roll_dice(5))
# Minimum amount possible is 5 (if each dice rolls a 1), and
# the maximum amount is 30 (if each dice rolls a 6)
assert my_module.roll_dice(5) >= 5 and my_module.roll_dice(5) <= 30
print("sum 0 dice:", my_module.roll_dice(0))


# Uppgift 4 (att skrivas)
print("\n----------- UPG 4 ---------------\n")

list_unsorted = [5, 3, 8, 1, 4, 2, 6, 7]
list_to_sort = list_unsorted
list_built_in_sort = list_unsorted

print("unsorted:\t\t", list_unsorted)

list_built_in_sort.sort()
print("bult-in sort:\t", list_built_in_sort)

print("my sort:\t\t", my_module.my_sort_list(list_unsorted))

assert list_to_sort == list_unsorted


# Uppgift 5 (att skrivas)
print("\n----------- UPG 5 ---------------\n")

sentence = "hello my name is bandodo"
bandit_sentence = my_module.bandit_language(sentence)
print("sentence:\t\t", sentence)
print("bandit version:\t", bandit_sentence)

# Test sentence from the exercise description
test_sentc = "jag talar rövarspråket"
assert my_module.bandit_language(test_sentc) == "jojagog totalolaror rorövovarorsospoproråkoketot"


# Uppgift 6 (givet)
print("\n----------- UPG 6 ---------------\n")

animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }

def make_bandit_dictionary(in_dictionary):

    bandit_dict = {}

    for key, value in in_dictionary.items():
        bandit_value_list = []
        for item in value:
            bandit_value_list.append(my_module.bandit_language(item))
        bandit_dict[key] = bandit_value_list

    return bandit_dict

print("original dict:", animals)
print("bandified dict:", my_module.make_bandit_dictionary(animals))

