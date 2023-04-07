string_input = input("please enter your string")
vowels_counter = 0;
for char in string_input:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels_counter += 1
print(vowels_counter)
