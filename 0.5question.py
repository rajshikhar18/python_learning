#find the longest word in sentence te
sentence = input("Enter the sentence:")
word = sentence.split()
longest_word =""
for word in word:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)
