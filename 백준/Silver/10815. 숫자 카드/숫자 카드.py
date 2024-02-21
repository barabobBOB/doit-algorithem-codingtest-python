import sys

# 입력 받기 최적화
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
nums = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return '1'
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return '0'

# 결과를 리스트에 저장
result = []
for num in nums:
    result.append(binary_search(A, num, 0, N-1))

# 결과 출력 최적화
print(' '.join(result))