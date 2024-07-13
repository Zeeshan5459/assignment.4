# Write a python program that reverses the order of
# words in a given sentence.
# for sentence= "python is fun":
# output  will be "fun is puthon"

reverse = "python is fun"
words = reverse.split()
Empty = ""
index = len(words) - 1
while index >= 0:
    Empty += words[index] + " " 
    index -= 1
print(Empty.strip()) 
