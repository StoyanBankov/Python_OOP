class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_position = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position == self.count - 1:
            raise StopIteration

        self.current_position += 1
        return self.current_position * self.step
