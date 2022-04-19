import random


class Sorter:
    sortable = []

    def __init__(self, sortable):
        self.sortable = sortable
        random.shuffle(self.sortable)

    def insertion_sort(self):
        unsorted = self.sortable[:]
        result = []
        for element in unsorted:
            was_inserted = False
            for i, _ in enumerate(result):
                if result[i] >= element:
                    result.insert(i, element)
                    was_inserted = True
                    break
            if not was_inserted:
                result.append(element)
            print(result)

        return result

    def quick_sort(self):


