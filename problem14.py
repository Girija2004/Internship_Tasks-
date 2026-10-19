M = int(input())
a = set(map(int, input().split()))

N = int(input())
b = set(map(int, input().split()))

for num in sorted(a ^ b):
    print(num)