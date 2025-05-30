# Дан односвязный линейный список и указатель на голову списка P1.
# Необходимо вставить значение M после каждого четвертого элемента списка, и
# вывести ссылку на последний элемент полученного списка P2.
class Node:
    def __init__(self, data):
        self.data = data  # значение текущего элемента
        self.next = None  # ссылка на следующий элемент

class LinkedList:
    def __init__(self):
        self.head = None  # изначально список пуст

    def append(self, data):#добавляет новый узел в конец списка
        new_node = Node(data)  # создаем новый узел с данными
        if not self.head:
            self.head = new_node  # если список пуст, новый узел становится головой
            return
        current = self.head #начинаем с головы списка
        while current.next:  # пока не достигнет последнего элемента
            current = current.next # к следующему узлу
        current.next = new_node  # добавляем новый узел в конец списка

    def insert_after_every_fourth(self, M): #вставляет элемент после каждого 4
        current = self.head
        count = 1  # счетчик элементов

        while current:
            if count == 4:
                new_node = Node(M) #новый узел
                new_node.next = current.next  # новый узел указывает на следующий элемент
                current.next = new_node  # предыдущий элемент теперь указывает на новый
                count = 0  # сброс счетчика после вставки
            current = current.next  # переходим к следующему элементу
            count += 1  # увеличиваем счетчик

    def get_last_element(self):#последний элемент
        current = self.head
        while current and current.next:
            current = current.next
        return current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
n = int(input("Введите количество элементов в списке (не менее 4): "))
M = int(input("Введите значение M: "))
for i in range(n):
    data = int(input(f"Введите значение для элемента {i+1}: "))
    ll.append(data)
ll.insert_after_every_fourth(M)
print("Содержимое списка после вставки:")
ll.display()
P2 = ll.get_last_element()
if P2:
    print(f"Значение последнего элемента: {P2}")
else:
    print("Список пуст.")
