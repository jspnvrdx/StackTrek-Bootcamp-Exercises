class PickItUp:
    @classmethod
    def sort(cls, array):
        length = len(array)
        for i in range(length):
          min_index = i
          for j in range(i + 1, length):
            if array[j].weight() > array[min_index].weight():
              min_index = j
          array[i], array[min_index] = array[min_index], array[i]
        return [item.name for item in array]


class Item:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def weight(self):
        return self.mass