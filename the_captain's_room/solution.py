k = int(input())
arr = list(map(int, input().split()))

room = (sum(set(arr)) * k - sum(arr)) // (k - 1)
print(room)
