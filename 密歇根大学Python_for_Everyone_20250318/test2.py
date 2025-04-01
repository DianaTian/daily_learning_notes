words = list()

file = open('romeo.txt')
for line in file:
    tmp = line.split()
    for word in tmp:
        if word not in words:
            words.append(word)

# words.sort()
# print(words)
print(sorted(words))

