"""Proyecto #02 de la materia de Algoritmos"""
import random
import time
# https://www.geeksforgeeks.org/sorting-algorithms/


class Sorting():
    """Clase encargada de proporcionar metodos con los algoritmos de ordenamiento"""

    def bubble(self, data):
        """Bubble sort algorithm - O(n2)"""
        sorted_data = list(data)
        size = len(sorted_data)
        for i in range(size):  # Traverse through all array elements
            for j in range(0, size - i - 1):  # Last i elements are already in place
                if sorted_data[j] > sorted_data[j + 1]:   # Swap if the element found is greater than the next element
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
        return sorted_data

    def insertion(self, data):
        """Insertion sort algorithm - O(n2)"""
        sorted_data = list(data)
        for i in range(1, len(sorted_data)):  # Traverse through 1 to last element
            key = sorted_data[i]  # Value to compare
            j = i-1  # Get a position before the current one
            while j >= 0 and key < sorted_data[j]:  # Compare value against element in list
                sorted_data[j + 1] = sorted_data[j]
                j -= 1
            sorted_data[j + 1] = key  # Insert value in correct position
        return sorted_data

    def selection(self, data):
        """Insertion sort algorithm - O(n2)"""
        sorted_data = list(data)
        size = len(sorted_data)
        for i in range(size):  # Traverse through all list elements
            min_idx = i
            for j in range(i+1, size):  # Traverse through unsorted sub-list
                if sorted_data[min_idx] > sorted_data[j]:  # Find lowest unsorted element
                    min_idx = j
            # Swap the minimum element with the first element
            sorted_data[i], sorted_data[min_idx] = sorted_data[min_idx], sorted_data[i]
        return sorted_data

    def merge(self, data):
        """Merge sort algorithm - O(n log n)"""
        sorted_data = list(data)
        size = len(sorted_data)
        if size > 1:  # Check until atomic element
            mid = size//2  # Finding the mid of the array
            left = sorted_data[:mid]  # Dividing the array elements
            right = sorted_data[mid:]  # into 2 halves

            left = self.merge(left)  # Sorting the first half
            right = self.merge(right)  # Sorting the second half

            # Copy data to temp arrays left[] and right[]
            left_pos = right_pos = current_pos = 0
            while left_pos < len(left) and right_pos < len(right):
                if left[left_pos] < right[right_pos]:
                    sorted_data[current_pos] = left[left_pos]
                    left_pos += 1
                else:
                    sorted_data[current_pos] = right[right_pos]
                    right_pos += 1
                current_pos += 1

            # Checking if any element was left
            while left_pos < len(left):
                sorted_data[current_pos] = left[left_pos]
                left_pos += 1
                current_pos += 1
            while right_pos < len(right):
                sorted_data[current_pos] = right[right_pos]
                right_pos += 1
                current_pos += 1

        return sorted_data

    def partition(self, data, low, high):
        """"""
        sorted_data = list(data)
        i = (low-1)         # index of smaller element
        pivot = sorted_data[high]     # pivot
        for j in range(low, high):
            if sorted_data[j] < pivot:  # If current element is smaller than the pivot
                i = i+1  # increment index of smaller element
                sorted_data[i], sorted_data[j] = sorted_data[j], sorted_data[i]
        sorted_data[i+1], sorted_data[high] = sorted_data[high], sorted_data[i+1]
        return (i+1), sorted_data

    def quick(self, data, low, high):
        """Merge sort algorithm - O(n log n)"""
        sorted_data = list(data)
        if low < high:
            # Partitioning index, sorted_data[pi] is now at right place
            pi, sorted_data = self.partition(sorted_data, low, high)
            # Separately sort elements before partition and after partition
            sorted_data = self.quick(sorted_data, low, pi-1)
            sorted_data = self.quick(sorted_data, pi+1, high)
        return sorted_data

    def shell(self, data):
        """Shell sort algorithm - O(n)"""
        sorted_data = list(data)
        size = len(sorted_data)
        gap = size // 2  # Start with a big gap, then reduce the gap

        while gap > 0:
            for i in range(gap, size):
                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = sorted_data[i]
                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while j >= gap and sorted_data[j - gap] > temp:
                    sorted_data[j] = sorted_data[j - gap]  # Swap elements
                    j -= gap
                    # put temp (the original a[i]) in its correct location
                sorted_data[j] = temp
            gap //= 2
        return sorted_data

    def heapify(self, data, n, i):
        sorted_data = list(data)
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and sorted_data[i] < sorted_data[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and sorted_data[largest] < sorted_data[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            sorted_data[i], sorted_data[largest] = sorted_data[largest], sorted_data[i]  # swap

            # Heapify the root.
            self.heapify(sorted_data, n, largest)

        return sorted_data

    def heap(self, data):
        """"""
        sorted_data = list(data)
        n = len(sorted_data)

        # Build a maxheap.
        for i in range(n, -1, -1):
            sorted_data = self.heapify(sorted_data, n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            sorted_data[i], sorted_data[0] = sorted_data[0], sorted_data[i]  # swap
            sorted_data = self.heapify(sorted_data, i, 0)

        return sorted_data

    def bucket(self, data):
        """Bucket sort algorithm - O(n)"""
        def get_first_digit(num):
            """"Internal function to get the first digit of a number"""
            while num >= 10:
                num /= 10
            return num

        sorted_data = list(data)
        arr = []
        slot_num = 10  # 10 means 10 slots, each
        # slot's size is 0.1
        for i in range(slot_num):
            arr.append([])
        # Put array elements in different buckets
        for element in sorted_data:
            index_b = int(get_first_digit(element))
            if index_b < len(arr):
                arr[index_b].append(element)
        # Sort individual buckets
        for i in range(slot_num):
            if i < len(arr):
                arr[i] = self.insertion(arr[i])
        # concatenate the result
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                sorted_data[k] = arr[i][j]
                k += 1
        return sorted_data


if __name__ == "__main__":
    data = [random.randrange(0, 100, 5) for i in range(5)]
    sort_by = Sorting()
    print("Initial data {}\n".format(data))

    start = time.time()
    new_data = sort_by.bubble(data)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nBubble time: {}\n".format(new_data, run_time))

    start = time.time()
    new_data = sort_by.insertion(data)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nInsertion time: {}\n".format(new_data, run_time))

    start = time.time()
    new_data = sort_by.selection(data)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nSelection time: {}\n".format(new_data, run_time))

    start = time.time()
    new_data = sort_by.merge(data)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nMerge time: {}\n".format(new_data, run_time))

    start = time.time()
    new_data = sort_by.quick(data, 0, len(data)-1)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nQuick time: {}\n".format(new_data, run_time))

    start = time.time()
    new_data = sort_by.shell(data)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nShell time: {}\n".format(new_data, run_time))

    start = time.time()
    new_data = sort_by.bucket(data)
    end = time.time()
    run_time = end - start
    print("Sorted data: {}\nBucket time: {}\n".format(new_data, run_time))
