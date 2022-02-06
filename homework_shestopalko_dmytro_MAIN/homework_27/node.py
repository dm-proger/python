class Node:
    def __init__(self, data, position = 0):
        self._data = data
        self._next = None
        self.position = position

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

object_01 = Node(93)
print(object_01.get_data())