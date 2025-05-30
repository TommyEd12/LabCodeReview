'''Даны две непустые очереди; начало и конец первой равны A1 и A2, 
авторой—A3 и A4. Очереди содержат одинаковое количество элементов.
Объединить очереди в одну,вкоторой элементы исходных 
очередей чередуются (начиная с первого элемента первой очереди).
Вывести ссылки на начало и конец полученной очереди. Новые объекты типа Node не создавать.'''
#Слишком длинные строки комментариев
class Node:
       
    def __init__(self, value):
        self.value = value
        self.next = None

def create_queue(n):
    # Очевидный комментарий, лучше указать в названии
    values = list(map(int, input(f"Введите {n} элементов(а) очереди через пробел: ").split()))
    head = Node(values[0])
    tail = head
    for value in values[1:]:
        tail.next = Node(value)
        tail = tail.next
    return head, tail
    #Множество очевидных комментариев
def merge_queues(A1, A3):
    #Название плохо отражает суть функции
    head = A1
    tail = None
    current1, current2 = A1, A3
    #Сокращенные названия

    while current1 and current2:
        next1, next2 = current1.next, current2.next
        current1.next = current2

        if next1:
            current2.next = next1
        else:
            tail = current2
        current1, current2 = next1, next2

    if not tail:
        tail = A1 if current1 else A3

    return head, tail
    #Множество очевидных комментариев

def print_queue(head):
    current = head
    #сокращенное название
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

n = int(input("Введите количество элементов в каждой очереди: "))

A1, A2 = create_queue(n)
A3, A4 = create_queue(n)

head, tail = merge_queues(A1, A3)

print("\nОбъединённая очередь:")
print_queue(head)
print(f"Head: {head.value}, Tail: {tail.value}")
#Множество очевидных комментариев

"""Введите количество элементов в каждой очереди: 4
Введите 4 элементов(а) очереди через пробел: 1 3 5 7
Введите 4 элементов(а) очереди через пробел: 2 4 6 8

Объединённая очередь:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
Head: 1, Tail: 8"""