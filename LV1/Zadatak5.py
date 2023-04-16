
with open('song.txt', 'r') as f:
    text = f.read()

words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

count = 0
for word, freq in word_counts.items():
    if freq == 1:
        count += 1
        print(word)

print("Broj riječi koje se pojavljuju samo jednom:", count)
