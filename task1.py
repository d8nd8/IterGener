# Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т. е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.main_list_i = 0
        self.inner_list_i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.main_list_i < len(self.list_of_list):
            if self.inner_list_i < len(self.list_of_list[self.main_list_i]):
                item = self.list_of_list[self.main_list_i][self.inner_list_i]
                self.inner_list_i += 1
                return item
            self.main_list_i += 1
            self.inner_list_i = 0

        raise StopIteration




def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()