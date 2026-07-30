#find the first repeating character in the string 
string = input("Enter the string:")
char_frequency ={}
for char in string:
    if char in char_frequency:
        char_frequency[char] +=1
    else:
        char_frequency[char] =1

for char in string:
    if char_frequency[char] >1:
        print(f"'{char}' is the first repeating character in the string")
        break 
    else:
        print("No repeating character found in the string")        