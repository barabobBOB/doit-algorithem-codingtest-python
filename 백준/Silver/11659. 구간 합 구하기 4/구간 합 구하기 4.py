import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

value_list = [0]
cut = 0

for i in numbers:
    cut += i
    value_list.append(cut)

for i in range(m):
    start, end = map(int, input().split())
    print(value_list[end] - value_list[start - 1])