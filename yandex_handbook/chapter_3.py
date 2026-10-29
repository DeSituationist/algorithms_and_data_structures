''' Множества '''
class HashBasedSet:
    def __init__(self):
        self.cap = 4
        self.buckets = [[] for _ in range(self.cap)]
        self.mask = self.cap - 1
        self.size = 0
        self.thres = self.cap * 2 // 3

    def Hash(self, x):
        return (x * 2654435761 & 0xFFFFFFFF) & self.mask

    def extend(self):
        old = self.buckets
        cap = self.cap * 2
        self.buckets = [[] for _ in range(cap)]
        self.cap = cap
        self.mask = cap - 1
        self.thres = cap * 2 // 3
        for b in old:
            for x in b:
                self.buckets[self.Hash(x)].append(x)

    def add_item(self, x):
        b = self.buckets[self.Hash(x)]
        for v in b:
            if v == x:
                return
        b.append(x)
        self.size += 1
        if self.size > self.thres:
            self.extend()

    def check_item(self, x):
        b = self.buckets[self.Hash(x)]
        for v in b:
            if v == x:
                return 1
        return 0
    
q = int(input())
s = HashBasedSet()

for _ in range(q):
    request = input().split(' ')
    to_do, item = request
    if to_do == '1': s.add_item(int(item))
    else: print(s.check_item(int(item)))

''' B '''
class ByteArraySet:
    def __init__(self):
        self.table = bytearray(1000001)
        self.size = 0
        
    def add_item(self, x):
        if self.table[x] == 0:
            self.table[x] = 1
            self.size += 1
            
    def check_item(self, x):
        return self.table[x]

n = int(input())
s = ByteArraySet()

for _ in range(n):
    row = list(map(int, input().split()))
    for x in row[1:]:
        s.add_item(x)

print(s.size)

''' C '''
import sys

data = sys.stdin.buffer.read().split()
it = iter(data) 

n = int(next(it))
k = int(next(it))

mask_bytes = bytearray(125001)

for _ in range(k):
    x = int(next(it))
    mask_bytes[x >> 3] |= (1 << (x & 7))

mask = int.from_bytes(mask_bytes, 'little')

for _ in range(n - 1):
    k = int(next(it))
    curr_bytes = bytearray(125001)
    
    for _ in range(k):
        x = int(next(it))
        curr_bytes[x >> 3] |= (1 << (x & 7))
        
    curr_mask = int.from_bytes(curr_bytes, 'little')
    mask &= curr_mask

print(mask.bit_count())

''' D '''
counts = {}
set_sizes = []
q = int(input())

for i in range(q):
    data = input().split()
    k, nums = data[0], set(data[1:])
    set_sizes.append(int(k))
    for _ in nums:
        counts[_] = counts.get(_, 0) + 1

vals = counts.values()
core_size = sum(1 for val in vals if val == q)

if any(1 < times < q for times in vals):
    print('NO')
else:
    print('YES')
    print(core_size)
    print(' '.join(str(set_size - core_size) for set_size in set_sizes))