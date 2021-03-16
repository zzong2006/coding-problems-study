import sys
from itertools import combinations

get_input = sys.stdin.readline

n, k = list(map(int, get_input().split()))
words = [set() for _ in range(n)]
unique_alpha = set()
for i in range(n):
    word = get_input().strip()
    for j in word:
        unique_alpha.add(j)
        if j != 'a' and j != 'n' and j != 't' and j != 'i' and j != 'c':
            words[i].add(j)



if k < 5:
    print(0)
else:
    remains_k = k - 5  # a, n, t, i, c
    for w in ['a', 'n', 't', 'i', 'c']: unique_alpha.remove(w)
    max_words = 0
    # print(unique_alpha)
    if len(unique_alpha) <= remains_k:
        print(n)
    else:
        for combs in combinations(unique_alpha, remains_k):
            new_words = set(combs)
            count = 0
            for word in words:
                if word.issubset(new_words):
                    count += 1
            max_words = max(max_words, count)

        print(max_words)