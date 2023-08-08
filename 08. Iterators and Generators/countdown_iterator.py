class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_position = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_position -= 1
        if self.current_position < 0:
            raise StopIteration

        return self.current_position
