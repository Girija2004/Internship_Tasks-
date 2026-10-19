
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    count1 = Counter(s1)
    count2 = Counter(s2)

    return sum((count1 - count2).values())


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        print(anagram(s))
