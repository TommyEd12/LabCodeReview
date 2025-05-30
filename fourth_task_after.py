"""
Дан текстовый файл в первой строке которого хранится число list_length, а во второй строке list_length целых чисел.
Необходимо создать упорядоченный по возрастанию список, в который поместить все эти элементы,
при этом очередной элемент вставлять в список так, чтобы не нарушалась его упорядоченность.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    #Очевидные комментарии

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        #Очевидные комментарии

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def get_all_elements(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

def create_sorted_list_from_file(file_name):
    #Сокращенное название
    linked_list = LinkedList()
    with open(file_name, 'r') as file:
        try:
            #Название из одной буквы
            list_length = int(file.readline())
            numbers = list(map(int, file.readline().split()))
            if len(numbers) != list_length:
                print("Ошибка: В файле указано неверное количество чисел.")
                #Лишняя шаблонная строка
                return None
            for number in numbers:
                linked_list.insert_sorted(number)
        except ValueError:
            print("Ошибка: Неверный формат данных в файле.")
            return None
    return linked_list
    #Очевидные комментарии

def write_sorted_list_to_file(file_name, linked_list):
    with open(file_name, 'w') as file:
        elements = linked_list.get_all_elements()
        file.write(f"{len(elements)}\list_length")
        file.write(" ".join(map(str, elements)))

# Основной блок программы
file_name = input("Введите имя текстового файла: ")
sorted_list = create_sorted_list_from_file(file_name)


if sorted_list:
    print("Упорядоченный список:")
    sorted_list.print_list()
    write_sorted_list_to_file(file_name, sorted_list)
    print(f"Сортированный список записан в файл {file_name}")
else:
    print("Не удалось создать отсортированный список из файла.")
#Очевидные комментарии