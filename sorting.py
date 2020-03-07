"""Proyecto #02 de la materia de Algoritmos"""
import random
import time
# https://www.geeksforgeeks.org/sorting-algorithms/


class Sorting():
    """Clase encargada de proporcionar metodos con los algoritmos de ordenamiento"""

    def bubble(self, data):
        """Bubble sort algorithm"""
        tmp_data = list(data)
        swapping_count = 1
        length_data = len(tmp_data)

        while swapping_count > 0:
            swapping_count = 0
            index = 1 # Start at position 2 of the list
            while index < length_data:
                tmp_vale = tmp_data[index]
                if tmp_data[index] < tmp_data[index-1]:
                    tmp_data[index] = tmp_data[index-1]
                    tmp_data[index-1] = tmp_vale
                    swapping_count += 1
                index += 1
        return tmp_data

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

    def partition(self, data, low, high):
        """"""
        tmp_data = list(data)
        i = (low-1)         # index of smaller element
        pivot = tmp_data[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than the pivot
            if tmp_data[j] < pivot:

                # increment index of smaller element
                i = i+1
                tmp_data[i], tmp_data[j] = tmp_data[j], tmp_data[i]

        tmp_data[i+1], tmp_data[high] = tmp_data[high], tmp_data[i+1]

        return (i+1), tmp_data

    def quick(self, data, low, high):
        """"""
        tmp_data = list(data)
        if low < high:

            # pi is partitioning index, tmp_data[p] is now
            # at right place
            pi, tmp_data = self.partition(tmp_data, low, high)

            # Separately sort elements before
            # partition and after partition
            tmp_data = self.quick(tmp_data, low, pi-1)
            tmp_data = self.quick(tmp_data, pi+1, high)

        return tmp_data

    def heapify(self, data, n, i):
        tmp_data = list(data)
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and tmp_data[i] < tmp_data[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and tmp_data[largest] < tmp_data[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            tmp_data[i], tmp_data[largest] = tmp_data[largest], tmp_data[i]  # swap

            # Heapify the root.
            self.heapify(tmp_data, n, largest)

        return tmp_data

    def heap(self, data):
        """"""
        tmp_data = list(data)
        n = len(tmp_data)

        # Build a maxheap.
        for i in range(n, -1, -1):
            tmp_data = self.heapify(tmp_data, n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            tmp_data[i], tmp_data[0] = tmp_data[0], tmp_data[i]  # swap
            tmp_data = self.heapify(tmp_data, i, 0)

        return tmp_data

    def bucket(self, data):
        """"""
        tmp_data = list(data)
        arr = []
        slot_num = 10  # 10 means 10 slots, each
        # slot's size is 0.1
        for i in range(slot_num):
            arr.append([])

        # Put array elements in different buckets
        for j in tmp_data:
            index_b = int(slot_num * j)
            if index_b < len(arr):
                arr[index_b].append(j)

        # Sort individual buckets
        for i in range(slot_num):
            if i < len(arr):
                arr[i] = self.insertion(arr[i])

        # concatenate the result
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                tmp_data[k] = arr[i][j]
                k += 1

        return tmp_data


if __name__ == "__main__":
    # data = random.sample(range(0, 1000000), 5)
    data = [random.randrange(0, 100, 5) for i in range(50)]
    sort_by = Sorting()
    print("Initial data {}\n".format(data))

    start = time.time()
    print(sort_by.insertion(data))
    end = time.time()
    insertion_time = end - start
    print("Insertion time: {}\n".format(insertion_time))

    start = time.time()
    print(sort_by.merge(data))
    end = time.time()
    insertion_time = end - start
    print("Merge time: {}\n".format(insertion_time))

    start = time.time()
    print(sort_by.quick(data, 0, len(data)-1))
    end = time.time()
    insertion_time = end - start
    print("Quick time: {}\n".format(insertion_time))

    start = time.time()
    print(sort_by.heap(data))
    end = time.time()
    insertion_time = end - start
    print("Heap time: {}\n".format(insertion_time))

    start = time.time()
    print(sort_by.bucket(data))
    end = time.time()
    insertion_time = end - start
    print("Bucket time: {}\n".format(insertion_time))

    start = time.time()
    print(sort_by.bubble(data))
    end = time.time()
    insertion_time = end - start
    print("Bubble time: {}\n".format(insertion_time))
