
def gemstones(arr):
    common = set(arr[0])

    for rock in arr[1:]:
        common = common.intersection(set(rock))

    return len(common)


if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input())

    result = gemstones(arr)
    print(result)
