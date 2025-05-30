class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
#Очевидные комментарии
#Отступы после классов

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    #Очевидные комментарии

    def insert_after_every_fourth(self, node_value):
        #Название переменной из одной буквы
        current = self.head
        count = 1

        while current:
            if count == 4:
                new_node = Node(node_value)
                new_node.next = current.next
                current.next = new_node
                count = 0
            current = current.next
            count += 1

    def get_last_element(self):
        current = self.head
        while current and current.next:
            current = current.next
        return current

    #Непонятное название метода
    def display_nodes(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#названия переменных из одной буквы
new_list = LinkedList()
list_length = int(input("Введите количество элементов в списке (не менее 4): "))
#Непонятный вывод для пользователя
node_value = int(input("Введите значение узла: "))
for i in range(list_length):
    data = int(input(f"Введите значение для элемента {i+1}: "))
    new_list.append(data)
new_list.insert_after_every_fourth(node_value)
print("Содержимое списка после вставки:")
new_list.display_nodes()
P2 = new_list.get_last_element()
if P2:
    #Непонятный вывод программы (ссылка на объект Node)
    print(f"Значение последнего элемента: {P2.data}")
else:
    print("Список пуст.")
