''' Односвязный список '''

'''
Изначально у вас есть пустой список. Далее вам поступает q запросов. Каждый запрос одного из следующих типов:

Запрос 1-ого типа: добавить число y после x-ого числа в списке. Если x = 0, то нужно сделать число y новым началом списка.
Запрос 2-ого типа: вывести число, которое находится на позиции x в списке.
Запрос 3-его типа: удалить число, которое находится на позиции x в списке.

После каждого запроса второго типа необходимо вывести число, являющееся ответом. Гарантируется, что в списке в этот момент находилось хотя бы x элементов.

Также гарантируется, что если вам поступил запрос первого или третьего типа, то список к этому моменту содержал хотя бы x элементов.

Формат ввода
Первая строка содержит единственное число q — количество запросов.
Далее следует q строк. Каждая из этих строк может иметь один из следующих видов:
Для запроса первого типа — "1 x y" (без кавычек)
Для запросов второго типа — "2 x" (без кавычек)
Для запроса третьего типа — "3 x" (без кавычек)

Формат вывода
Вывод должен состоять из count строк, где count — количество запросов второго типа. Каждая строка должна содержать ответ на соответствующий запрос в формате value (где value — число, которое находится на позиции x).
'''
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None):
        self.val: int = val
        self.next: "ListNode | None" = next

class LinkedList:
    def __init__(self):
        self.front: ListNode | None = None
        self.size: int = 0
    
    def add_node(self, val: int, position: int):
        new_node = ListNode(val)

        if position == 0:
            new_node.next = self.front
            self.front = new_node
            self.size += 1
            return

        position -= 1
        curr_node, curr_ind = self.front, 0
        while curr_node and curr_ind <= self.size:
            if curr_ind == position:
                tmp_node = curr_node.next
                new_node.next = tmp_node
                curr_node.next = new_node
                self.size += 1
                break
            curr_node = curr_node.next
            curr_ind += 1

def find(self, position: int) -> int:
    position -= 1
    curr_node, curr_ind = self.front, 0
    while curr_node and curr_ind < position:
        curr_node = curr_node.next
        curr_ind += 1
    return curr_node.val

def remove(self, position: int):
    position -= 1
    if position == 0:
        if self.front:
            self.front = self.front.next
            self.size -= 1
        return

    curr_node, curr_ind = self.front, 0
    while curr_node.next and curr_ind <= self.size:
        if curr_ind == position - 1:
            curr_node.next = curr_node.next.next if curr_node.next.next else None
            self.size -= 1
            break
        curr_node = curr_node.next
        curr_ind += 1
    
n = int(input())
llist = LinkedList()
for _ in range(n):
    a, b, *rest = input().split()
    c = rest[0] if rest else None
    match a:
        case '1':
            llist.add_node(int(c), int(b))
        case '2':
            print(llist.find(int(b)))
        case '3':
            llist.remove(int(b))

'''
    Дан массив a, состоящий из n чисел. Необходимо найти две пары индексов i1 < j1 и i2 < j2 таких, что a[i1] - a[j1] минимально возможное и a[i2] - a[j2] максимально возможное.

    Формат ввода

    Первая строка содержит единственное число n — количество чисел в массиве.

    Вторая строка содержит n разделённых пробелом чисел a[i], где a[i] — число на i-ой позиции в массиве a.

    Формат вывода

    Первая строка вывода должна содержать два разделённых пробелом числа i1 и j1.
    Если подходящих пар несколько, то нужно выбрать пару с минимальным значением i1.
    Если пар с минимальным значением i1 несколько, то нужно выбрать пару с минимальным значением j1.

    Вторая строка вывода должна содержать два разделённых пробелом числа i2 и j2.
    Если подходящих пар несколько, то нужно выбрать пару с минимальным значением i2.
    Если пар с минимальным значением i2 несколько, то нужно выбрать пару с минимальным значением j2.
'''

n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
min_idx = 0

best_diff = float('inf')
best_i = -1
best_j = -1

for j in range(1, n):
    diff = min_val - arr[j]

    if diff < best_diff:
        best_diff = diff
        best_i = min_idx
        best_j = j
    elif diff == best_diff:

        if min_idx < best_i or (min_idx == best_i and j < best_j):
            best_i = min_idx
            best_j = j

    if arr[j] < min_val:
        min_val = arr[j]
        min_idx = j

print(best_i + 1, best_j + 1)