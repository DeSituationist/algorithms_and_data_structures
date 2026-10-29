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