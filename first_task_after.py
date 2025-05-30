"""Дана вершина A1 стека (если стек пуст, то A1 = null). Извлечь из стека 
все элементы и вывести их значения.
Вывести также количество извлеченных элементов N (для пустого стека вывести 0).
После извлечения элементов из стека освобождать ресурсы, 
которые они использовали, вызывая для этих элементов метод Dispose."""
#Строчки комментариев слишком длинные, не было docstring
import gc
import random

class Node:
    def __init__(self, data=None, next_node=None):
        #Переопредление встроенной функции next
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        #Неправильное название
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            #название переменной неправильное
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            #Название переменное неверное
            popped_node = self.head
            self.head = self.head.next_node
            popped_node.next_node = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def dispose(self):
        gc.collect()

#Грамматическая ошибка в название переменной
stack = Stack()
for i in range(random.randint(0, 20)): # Убран очевидный комментарий
    stack.push(random.randint(1,100))
#Переменная из одной буквы
stack_length = 0
while not stack.is_empty():
    print(stack.pop())
    stack_length += 1
print (stack_length)
stack.dispose()