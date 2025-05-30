"""Даны ссылки A1 и A2 на барьерный и текущий элементы непустогодвусвязногосписка, причем текущий элемент не совпадает
 с барьерным. Включить в класс IntListB функцию DeleteCurrent целого типа, удаляющуюиз списка
 текущий элемент и возвращающую его значение. Текущим становится следующий элемент или, если следующий элемент является
 барьерным, предыдущий элемент списка. Функция также вызывает для удаленного элемента метод Dispose. Если текущим
 элементом является барьерный элемент, то функция не выполняет никаких действий и возвращает 0. Спомощью этой функции,
 а также метода IsBarrier логического типа (возвращает true, если текущий элемент списка является его барьерным
 элементом, и false в противном случае), удалить из исходного списка пять элементов (или все элементы, если их менее
 пяти) и вывести их значения. Вывести также ссылку на новый текущий элемент списка.
 Описать класс IntListB, содержащий следующие члены:
 • закрытые поля barrier и current типа Node (барьерный и текущий элементысписка);
 • конструктор с параметрами aBarrier и aCurrent — барьерным и текущим элементами существующего списка;
• процедура InsertLast(D), которая добавляет новый элемент со значением D в конец списка (D — входной параметр целого
типа, добавленный элемент становится текущим);
• процедура Put (без параметров), которая выводит ссылку на поле current, используя метод Put класса PT."""
class Node:
    """Класс, представляющий узел двусвязного списка с барьерным элементом."""

    def __init__(self, data):
        self.data = data  # Данные узла
        self.prev = None  # Ссылка на предыдущий узел
        self.next = None  # Ссылка на следующий узел

    def dispose(self):
        """Метод для удаления узла (в Python сборка мусора делает это автоматически)."""
        del self


class IntListB:
    """Класс, реализующий двусвязный список с барьерным элементом."""

    def __init__(self):
        self.barrier = Node(0)  # Создаем барьерный узел
        self.barrier.next = self.barrier  # Связываем барьер с самим собой
        self.barrier.prev = self.barrier
        self.current = self.barrier  # Текущий элемент указывает на барьер

    def append(self, data):
        """Добавляет новый узел перед барьерным элементом."""
        new_node = Node(data)
        last = self.barrier.prev  # Последний элемент перед барьером

        last.next = new_node
        new_node.prev = last
        new_node.next = self.barrier
        self.barrier.prev = new_node

        if self.current == self.barrier:
            self.current = new_node  # Если список был пуст, текущий узел указывает на новый

    def is_barrier(self, node):
        """Проверяет, является ли узел барьерным."""
        return node == self.barrier

    def delete_current(self):
        """Удаляет текущий элемент, возвращает его значение и обновляет текущий узел."""
        if self.is_barrier(self.current):
            return 0  # Барьерный элемент нельзя удалять

        deleted_node = self.current
        value = deleted_node.data

        prev_node = deleted_node.prev
        next_node = deleted_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        if next_node != self.barrier:
            self.current = next_node  # Следующий узел становится текущим
        else:
            self.current = prev_node  # Если следующий узел барьерный, текущим становится предыдущий

        deleted_node.dispose()  # Удаление узла
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
    L = IntListB()

    # Ввод данных в список
    n = int(input("Введите количество элементов списка: "))
    for i in range(n):
        data = input(f"Введите элемент {i + 1}: ")
        L.append(data)

    print("\nИсходный список:")
    L.display()

    # Удаление до 5 элементов из списка
    deleted_values = []
    for _ in range(5):
        if L.is_barrier(L.current):
            break  # Прекращаем, если список пуст
        deleted_values.append(L.delete_current())

    print("\nУдаленные элементы:", deleted_values)
    print("\nСписок после удаления:")
    L.display()

    print("\nТекущий элемент после удаления:", L.current.data if not L.is_barrier(L.current) else "null")
