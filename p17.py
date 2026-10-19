
def separateNumbers(s):
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        result = str(first)

        while len(result) < len(s):
            current += 1
            result += str(current)

        if result == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
