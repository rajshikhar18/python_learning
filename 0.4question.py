# checking anagram 
string1 = input("Enter the string1: ")
string2 = input("Enter the string2: ")

dict1 ={}
for char in string1:
    if char in dict1:
        dict1[char] +=1
    else:
        dict1[char] =1


dict2 ={}
for char in string2:
    if char in dict2:
        dict2[char] +=1
    else:
        dict2[char] =1

if dict1 == dict2:
    print("The two strings are anagrams")
else:
    print("The two strings are not anagrams")