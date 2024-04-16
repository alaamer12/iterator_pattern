# Define an interface for creating an iterator
class Iterator:
    def __init__(self):
        pass

    def has_next(self):
        pass

    def next(self):
        pass


# Concrete implementation of Iterator interface
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration()


# Define an interface for creating an iterable
class Iterable:
    def __init__(self):
        pass

    def create_iterator(self):
        pass


# Concrete implementation of Iterable interface
class ConcreteIterable(Iterable):
    def __init__(self, collection):
        super().__init__()
        self._collection = collection

    def create_iterator(self):
        return ConcreteIterator(self._collection)


# Example usage
if __name__ == "__main__":
    # Create an iterable object
    iterable = ConcreteIterable([1, 2, 3, 4, 5])

    # Get an iterator from the iterable
    iterator = iterable.create_iterator()

    # Iterate over the collection using the iterator
    while iterator.has_next():
        print(iterator.next())
