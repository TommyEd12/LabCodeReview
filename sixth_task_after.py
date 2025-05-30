"""Даны ссылки A1 и A2 на барьерный и текущий элементы 
непустогодвусвязногосписка, причем текущий элемент не совпадает
 с барьерным. Включить в класс IntListB функцию DeleteCurrent целого типа, удаляющуюиз списка
 текущий элемент и возвращающую его значение.
 Текущим становится следующий элемент или, если следующий элемент является
 барьерным, предыдущий элемент списка. 
 Функция также вызывает для удаленного элемента метод Dispose. Если текущим
 элементом является барьерный элемент, 
 то функция не выполняет никаких действий и возвращает 0. Спомощью этой функции,
 а также метода IsBarrier логического 
 типа (возвращает true, если текущий элемент списка является его барьерным
 элементом, и false в противном случае), 
 удалить из исходного списка пять элементов (или все элементы, если их менее
 пяти) и вывести их значения. Вывести также ссылку на новый текущий элемент списка.
 Описать класс IntListB, содержащий следующие члены:
 • закрытые поля barrier и current типа Node (барьерный и текущий элементысписка);
 • конструктор с параметрами aBarrier и aCurrent — барьерным
  и текущим элементами существующего списка;
• процедура InsertLast(D), которая добавляет новый
 элемент со значением D в конец списка (D — входной параметр целого
типа, добавленный элемент становится текущим);
• процедура Put (без параметров), которая выводит
 ссылку на поле current, используя метод Put класса PT."""
#Длинные строки комментариев
class Node:
    """Класс, представляющий узел двусвязного списка с барьерным элементом."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    #Очевидные комментарии

    def dispose(self):
        """Метод для удаления узла (в Python сборка мусора делает это автоматически)."""
        del self


class IntListB:
    """Класс, реализующий двусвязный список с барьерным элементом."""

    def __init__(self):
        self.barrier = Node(0)
        self.barrier.next = self.barrier
        self.barrier.prev = self.barrier
        self.current = self.barrier
    #Очевидные комментарии

    def append(self, data):
        """Добавляет новый узел перед барьерным элементом."""
        new_node = Node(data)
        last = self.barrier.prev

        last.next = new_node
        new_node.prev = last
        new_node.next = self.barrier
        self.barrier.prev = new_node

        if self.current == self.barrier:
            self.current = new_node  # Если список был пуст, текущий узел указывает на новый

    def is_barrier(self, node):
        return node == self.barrier

    def delete_current(self):
        """Удаляет текущий элемент, возвращает его значение и обновляет текущий узел."""
        if self.is_barrier(self.current):
            return 0  # Барьерный элемент нельзя удалять

        deleted_node = self.current
        value = deleted_node.data
        #Сокрещнное название
        previous_node = deleted_node.prev
        next_node = deleted_node.next

        previous_node.next = next_node
        next_node.prev = previous_node

        if next_node != self.barrier:
            self.current = next_node  # Следующий узел становится текущим
        else:
            self.current = previous_node  # Если
            #следующий узел
            #барьерный, текущим становится предыдущий

            #Длинная строчка
        deleted_node.dispose()
        return value

    def display(self):
        """Выводит список на экран, исключая барьерный элемент."""
        current = self.barrier.next
        while current != self.barrier:
            if current == self.current:
                print(f"[{current.data}]", end=" <-> ")  # Выделяем текущий элемент
            else:
                print(current.data, end=" <-> ")
            current = current.next
        print("(barrier)")


# Пользовательский интерфейс
if __name__ == "__main__":
    #Название переменной из одной буквы
    new_list = IntListB()

    #Название переменной из одной буквы
    list_length = int(input("Введите количество элементов списка: "))
    for i in range(list_length):
        data = input(f"Введите элемент {i + 1}: ")
        new_list.append(data)

    print("\nИсходный список:")
    new_list.display()

    deleted_values = []
    for _ in range(5):
        if new_list.is_barrier(new_list.current):
            break
        deleted_values.append(new_list.delete_current())

    print("\nУдаленные элементы:", deleted_values)
    print("\nСписок после удаления:")
    new_list.display()

    print("\nТекущий элемент после удаления:", new_list.current.data
    if not new_list.is_barrier(new_list.current) else "null")
    #Длинная строка
    #Очевидные комментарии
