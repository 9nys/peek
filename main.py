class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self._next_item = next(self.iterator)

    def __iter__(self):
        return self

    def __next__(self):
        current_item = self._next_item
        try:
            self._next_item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            self._next_item = next(self.iterator)
        return current_item

    def peek(self):
        return self._next_item


iterable = ["a", "b", "c"]
cyclic_iter = CyclicIterator(iterable)
for _ in range(5):
    print(cyclic_iter.peek(), next(cyclic_iter))
