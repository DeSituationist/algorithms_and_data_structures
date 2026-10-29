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