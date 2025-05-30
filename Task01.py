# Дана вершина A1 стека (если стек пуст, то A1 = null). Извлечь из стека все элементы и вывести их значения.
# Вывести также количество извлеченных элементов N (для пустого стека вывести 0).
# После извлечения элементов из стека освобождать ресурсы, которые они использовали, вызывая для этих элементов метод Dispose.

import gc
import random

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def dispose(self):
        gc.collect()


stek = Stack()
for i in range(random.randint(0, 20)): # Заполнение стека
    stek.push(random.randint(1,100))
n = 0
while not stek.isempty():
    print(stek.pop())
    n += 1
print (n)
stek.dispose()