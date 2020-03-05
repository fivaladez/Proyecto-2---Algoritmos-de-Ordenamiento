"""Proyecto #02 de la materia de Algoritmos"""
import random
import time
# https://www.geeksforgeeks.org/sorting-algorithms/


class Sorting():
    """Clase encargada de proporcionar metodos con los algoritmos de ordenamiento"""

    def insertion(self, data):
        """"""
        tmp_data = list(data)
        # Traverse through 1 to len(tmp_data)
        for position in range(1, len(tmp_data)):
            key = tmp_data[position]
            # Move elements of tmp_data[0..position-1], that are
            # greater than key, to one position ahead of their current position
            last_position = position-1
            while last_position >= 0 and key < tmp_data[last_position]:
                tmp_data[last_position + 1] = tmp_data[last_position]
                last_position -= 1
            tmp_data[last_position + 1] = key

        return tmp_data

    def merge(self, data):
        """"""
        tmp_data = list(data)
        if len(tmp_data) > 1:
            mid = len(tmp_data)//2  # Finding the mid of the array
            left = tmp_data[:mid]  # Dividing the array elements
            right = tmp_data[mid:]  # into 2 halves

            left = self.merge(left)  # Sorting the first half
            right = self.merge(right)  # Sorting the second half

            left_pos = right_pos = current_pos = 0
            # Copy data to temp arrays left[] and right[]
            while left_pos < len(left) and right_pos < len(right):
                if left[left_pos] < right[right_pos]:
                    tmp_data[current_pos] = left[left_pos]
                    left_pos += 1
                else:
                    tmp_data[current_pos] = right[right_pos]
                    right_pos += 1
                current_pos += 1

            # Checking if any element was left
            while left_pos < len(left):
                tmp_data[current_pos] = left[left_pos]
                left_pos += 1
                current_pos += 1

            while right_pos < len(right):
                tmp_data[current_pos] = right[right_pos]
                right_pos += 1
                current_pos += 1

        return tmp_data

    def quick(self, data):
        """"""
        pass

    def heap(self, data):
        """"""
        pass

    def bucket(self, data):
        """"""
        pass


if __name__ == "__main__":
    # data = random.sample(range(0, 1000000), 5)
    data = [random.randrange(0, 10, 1) for i in range(5)]
    sort_by = Sorting()
    print("Initial data {}\n".format(data))

    start = time.time()
    print(sort_by.insertion(data))
    end = time.time()
    insertion_time = end - start
    # print("{}".format(insertion_time))

    start = time.time()
    print(sort_by.merge(data))
    end = time.time()
    insertion_time = end - start
    # print("{}".format(insertion_time))
