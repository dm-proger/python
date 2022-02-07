
class UnorderedList(BasicList):
    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())


class OrderedList(BasicList):
    def add(self, item):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self._head)
            self._head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found


def main():
    ...


if __name__ == '__main__':
    main()