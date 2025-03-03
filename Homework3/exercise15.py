import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
    return name.capitalize()

capitalized_suffixes = list(map(capitalize_suffix, suffixes))

random_names = [create_fantasy_name(prefixes, capitalized_suffixes) for _ in range(10)]

def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return name1 + ' ' + name2

filtered_names = list(filter(fire_in_name, random_names))

reduced_names = reduce(concatenate_names, filtered_names) if filtered_names else ""

def display_name_info():
    print("Generated Fantasy Names:")
    for name in random_names:
        print(name)
    
    print("\nFiltered Names (Containing 'Fire'):")
    for name in filtered_names:
        print(name)
    
    print("\nConcatenated Filtered Names:")
    print(reduced_names)

display_name_info()
