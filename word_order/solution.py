from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

word_counts = Counter(words)

print(len(word_counts))
print(' '.join(str(i) for i in word_counts.values()))
