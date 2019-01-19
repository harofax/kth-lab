
import copy
import math
import random

random.seed()


# Uppgift 1 (givet)
def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x

x_list = [11, 22, 33, 44]
x = 11
y = 22
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))


# Uppgift 2 (att skrivas)
def my_function(x):
    return math.sin(x)**2 + x**2


# Uppgift 3 (att skrivas)
def roll_dice(n):
    dice_sum = 0
    for i in range(n):
        dice_sum += random.randint(1, 6)
    return dice_sum

# Uppgift 4 (att skrivas)
def my_sort_list(list):
    list_length = len(list)
    sorted_list = list

    # Go through the list
    for i in range(list_length):

        # go to elements that are already sorted,
        # so it doesn't go through already sorted elements
        for j in range(list_length-i-1):

            # go through unsorted elements (length of list - i - 1)
            # swap an element if the next one is greater
            if sorted_list[j] > sorted_list[j+1]:
                # we could make a temporary variable to swap but this
                # looks cleaner
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]

    return sorted_list


# Uppgift 5 (att skrivas)

def bandit_language(sentence):
    vowels = ["a", "e", "i", "o", "u", "å", "ä", "ö"]
    bandit_sentence = ""

    for letter in sentence:

        if not letter in vowels and letter != " ":
            bandit_letter = letter + "o" + letter
            bandit_sentence += bandit_letter
        else:
            bandit_sentence += letter

    return bandit_sentence

# Uppgift 6

def make_bandit_dictionary(in_dictionary):

    bandit_dict = {}

    for key, value in in_dictionary.items():
        bandit_value_list = []
        for item in value:
            bandit_value_list.append(bandit_language(item))
        bandit_dict[key] = bandit_value_list

    return bandit_dict

