n = int(input())
words = []
counts = {}

for _ in range(n):
    word = input().strip()

    if word not in counts:
        words.append(word)
        counts[word] = 1
    else:
        counts[word] += 1

print(len(counts))
print(*(counts[word] for word in words))