class MyCollection:
    def __init__(self):
        self.items = list(range(20))

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__", self._count)
        try:
            item = self._items[self._count]
        except IndexError:
            self._count = 0
            raise StopIteration
        else:
            self._count += 1
            return item



def main():
    my_collection = MyCollection()
    for item in my_collection:
        print(item)

    for item in my_collection:
        print(item)


if __name__ == "__main__":
    main()