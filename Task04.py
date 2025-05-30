"""
Дан текстовый файл в первой строке которого хранится число n, а во второй строке n целых чисел.
Необходимо создать упорядоченный по возрастанию список, в который поместить все эти элементы,
при этом очередной элемент вставлять в список так, чтобы не нарушалась его упорядоченность.
"""

class Node:
    def __init__(self, data):
        self.data = data  # Хранение данных узла
        self.next = None  # Указатель на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def insert_sorted(self, data):
        new_node = Node(data)  # Создаем новый узел
        if not self.head or self.head.data >= data:  # Если список пуст или новый элемент меньше головы
            new_node.next = self.head  # Новый узел становится головой
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:  # Идем по списку, пока не найдем место для вставки
                current = current.next
            new_node.next = current.next  # Новый узел указывает на следующий элемент
            current.next = new_node  # Текущий узел теперь ссылается на новый узел

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
    ll = LinkedList()
    with open(file_name, 'r') as file:
        try:
            n = int(file.readline())  # Читаем количество чисел
            numbers = list(map(int, file.readline().split()))  # Читаем числа во второй строке

            # Проверка на количество чисел
            if len(numbers) != n:
                print(f"Ошибка: В файле указано неверное количество чисел.")
                return None

            for number in numbers:
                ll.insert_sorted(number)  # Вставляем каждый элемент в упорядоченный список
        except ValueError:
            print("Ошибка: Неверный формат данных в файле.")
            return None
    return ll

def write_sorted_list_to_file(file_name, ll):
    with open(file_name, 'w') as file:
        elements = ll.get_all_elements()  # Получаем все элементы списка
        file.write(f"{len(elements)}\n")  # Записываем количество элементов
        file.write(" ".join(map(str, elements)))  # Записываем элементы списка через пробел

# Основной блок программы
file_name = input("Введите имя текстового файла: ")  # Вводим имя файла
sorted_list = create_sorted_list_from_file(file_name)  # Создаем упорядоченный список

# Если список создан успешно, продолжаем обработку
if sorted_list:
    print("Упорядоченный список:")
    sorted_list.print_list()  # Выводим список

    # Записываем отсортированный список обратно в файл
    write_sorted_list_to_file(file_name, sorted_list)
    print(f"Сортированный список записан в файл {file_name}")
else:
    print("Не удалось создать отсортированный список из файла.")
