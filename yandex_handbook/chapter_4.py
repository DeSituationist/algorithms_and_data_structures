''' Словарь '''
dt = {}
n = int(input())
for i in range(n):
    request = input().split()
    to_do = request[0]
    x = request[1]
    if to_do == '1':
        y = request[2]
        dt[x] = y
    else:
        print(dt.get(x, -1))

''' B '''
dt = {}
n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    dt[num] = dt.get(num, 0) + 1

mx = max(dt.values())
print(sorted([key for key, val in dt.items() if val == mx])[0])