from typing import List


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.text: List = []
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if len(self.text) >= self.number:
            raise StopIteration

        if self.index < len(self.sequence):
            self.text.append(self.sequence[self.index])
            return self.text[self.index]

        self.index = 0
        self.text.append(self.sequence[self.index])
        return self.text[self.index]
