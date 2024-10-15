# Write a Python program to count the occurrences of each word in a given sentence

sentence = input("Enter a sentence : ")

words = sentence.lower().split()

word_count = {} # Dictionary created. Alternate way to create dictionary is "word_count = dict()"

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")