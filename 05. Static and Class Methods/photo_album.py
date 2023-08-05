import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos: List[List] = self.__initialize_matrix()
        self.current_page_index = 0

    def __initialize_matrix(self):
        matrix = []

        for _ in range(self.pages):
            matrix.append([])

        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label:str):
        if len(self.photos[self.current_page_index]) == 4:
            self.current_page_index += 1

        try:
            self.photos[self.current_page_index].append(label)
            return f"{label} photo added successfully on page " \
                   f"{self.current_page_index+1} slot {len(self.photos[self.current_page_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        result = "-"*11 + "\n"

        for page in self.photos:
            result += ' '.join(["[]" for photo_name in page]) + "\n"
            result += "-" * 11 + "\n"

        return result
