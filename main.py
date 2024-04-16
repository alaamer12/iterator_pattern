from __future__ import annotations
from typing import Any, Iterable, List, Optional


class Iterator:
    def __init__(self, collection: Iterable):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()


class IterableCollection:
    def __init__(self):
        self._items: List[Any] = []

    def add_item(self, item: Any):
        self._items.append(item)

    def __iter__(self):
        return Iterator(self._items)


# Example usage
collection = IterableCollection()
collection.add_item("Apple")
collection.add_item("Banana")
collection.add_item("Orange")

for item in collection:
    print(item)
