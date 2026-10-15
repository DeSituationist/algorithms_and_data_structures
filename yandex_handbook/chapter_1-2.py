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

'''
    Дан массив a, состоящий из n чисел, и q запросов. Каждый запрос состоит из одного целого числа x_i.
    Найдите и выведите индекс p_i, который является первым, самым левым, вхождением числа x_i в массив a. Если x_i не встречается среди элементов массива, то p_i = -1.
    Формат ввода
    Первая строка содержит два разделённых пробелом числа n и q — количество чисел в массиве и количество запросов соответственно.
    Вторая строка содержит n чисел a_i, где a_i — число на i-й позиции в массиве a. Числа разделены пробелами.
    Далее идут q строк, каждая строка содержит ровно одно число x_i — очередной запрос.
    Формат вывода
    Для каждого запроса выведите p_i — индекс первого (самого левого) вхождения x_i в массив, или -1, если такого числа нет.
'''
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None):
        self.val: int = val
        self.next: "ListNode | None" = next

class LinkedList:
    def __init__(self, size, arr: list[int]):
        self.front = ListNode(arr[0])
        self.size: int = size
        curr_node = self.front
        for _ in range(1, self.size):
            curr_node.next = ListNode(arr[_])
            curr_node = curr_node.next
            
        self.first_pos = {}
        curr_node, curr_ind = self.front, 1
        while curr_node is not None:
            if curr_node.val not in self.first_pos:
                self.first_pos[curr_node.val] = curr_ind
            curr_node = curr_node.next
            curr_ind += 1

    def search(self, val: int) -> int:
        return self.first_pos.get(val, -1)

n, q = input().split(' ')
arr = list(map(int, input().split(' ')))
llist = LinkedList(int(n), arr)
for _ in range(int(q)):
    print(llist.search(int(input())))

'''
    Дан массив a, состоящий из n чисел.
    Для каждой позиции i (1 ≤ i ≤ n) вычислите величину
    text
    b_i = min(a[1], a[2], …, a[i])
    То есть b_i — минимум среди первых i элементов массива (префиксный минимум).
    Формат ввода
    Первая строка содержит единственное число n — количество чисел в массиве.
    Вторая строка содержит n чисел a_i, где a_i — число на i-й позиции в массиве a. Числа разделены пробелами.
    Формат вывода
    В оригинале не указан, но подразумевается: вывести n чисел b_1, b_2, …, b_n, разделённых пробелами (или каждое на новой строке — зависит от тестов).
'''
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None):
        self.val: int = val
        self.next: "ListNode | None" = next

class LinkedList:
    def __init__(self, size, arr: list[int]):
        self.front = ListNode(arr[0])
        self.size: int = size
        curr_node = self.front
        for _ in range(1, self.size):
            curr_node.next = ListNode(arr[_])
            curr_node = curr_node.next

    def min_before(self):
        curr_min = self.front.val
        curr_node, res = self.front, ''
        while curr_node is not None:
            if curr_node.val < curr_min:
                res += f' {curr_node.val}'
                curr_min = curr_node.val
            else:
                res += f' {curr_min}'
            curr_node = curr_node.next
        return res

n = int(input())
arr = list(map(int, input().split(' ')))
llist = LinkedList(n, arr)
print(llist.min_before())

'''
    Дан массив a, состоящий из n чисел. Позиция i является локальным минимум, если для нее выполнены условия 2≤i≤n−1 и a_{i−1}>a_i<a_{i+1}. 
    Требуется удалить из массива все элементы, стоящие в позициях локальных минимумов, определённых относительно исходного массива. 
    Формат ввода Первая строка содержит единственное число n -- количество чисел в массиве. Вторая строка содержит n, разделённых пробелами, чисел a_i, где a_i -- число на i-й позиции в массиве a. 
    Ограничения: 3≤n≤10^5; 1≤a_i≤10^5 для всех 1≤i≤n.
'''
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None, prev: "ListNode | None" = None):
        self.val: int = val
        self.next: "ListNode | None" = next
        self.prev: "ListNode | None" = prev

class LinkedList:
    def __init__(self, size, arr: list[int]):
        self.front = ListNode(arr[0])
        self.size: int = size
        curr_node = self.front
        for _ in range(1, self.size):
            new_node = ListNode(arr[_])
            curr_node.next = new_node
            new_node.prev = curr_node
            curr_node = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_mins(self):
        to_remove = []
        curr_node = self.front.next   

        while curr_node and curr_node.next:
            if curr_node.prev.val > curr_node.val and curr_node.next.val > curr_node.val:
                to_remove.append(curr_node)
            curr_node = curr_node.next
            
        for node in to_remove:
            self.remove(node)
            self.size -= 1

    def __str__(self):
        curr_node = self.front
        vals = []
        while curr_node is not None:
            vals.append(curr_node.val)
            curr_node = curr_node.next
        return ' '.join(str(v) for v in vals)

n = int(input())
arr = list(map(int, input().split(' ')))
llist = LinkedList(n, arr)
llist.remove_mins()
print(llist.size)
print(llist)