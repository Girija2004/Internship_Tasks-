
if __name__ == '__main__':
    s = input()

    from collections import Counter

    count = Counter(s)

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for char, freq in result[:3]:
        print(char, freq)
