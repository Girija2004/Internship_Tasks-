
def pangrams(s):
    letters = set(s.lower())

    if len(set('abcdefghijklmnopqrstuvwxyz') & letters) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
