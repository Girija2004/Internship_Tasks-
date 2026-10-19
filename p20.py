import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        number = input()
        if re.fullmatch(r'[789]\d{9}', number):
            print("YES")
        else:
            print("NO")