class Searching:
    def linear_search(self, array, key):
        """
        Returns an integer representing the index of the key in the array. 
        If the key is not found, returns -1.
        """
        for index, value in enumerate(array):
            if value == key:
                return index
        return -1

    def binary_search(self, array, key):
        """
        Returns an integer representing the index of the key in the array. 
        If the key is not found, returns -1.
        """
        start = 0
        end = len(array) - 1
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def jump_search(self, array, key):
        """
        Returns an integer representing the index of the key in the array. 
        If the key is not found, returns -1.
        """
        step = 0
        while array[step] < key:
            step += 1
        index = step
        while index < len(array):
            if array[index] == key:
                return index
            index += step
        return -1


class Sorting:
    def bubble_sort(self, array):
        """
        Sorts the given list using the bubble sort algorithm.
        """
        length = len(array)
        for i in range(length - 1):
            for j in range(0, length - i - 1):
                if array[j] >= array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

    def insertion_sort(self, array):
        """
        Sorts the given list using the insertion sort algorithm.
        """
        length = len(array)
        for i in range(1, length):
            temp = array[i]
            j = i - 1
            while j >= 0 and temp < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp

    def selection_sort(self, array):
        """
        Sorts the given list using the selection sort algorithm.
        """
        length = len(array)
        for i in range(length - 1):
            min_index = i
            for j in range(i + 1, length):
                if array[j] < array[min_index]:
                    min_index = j
            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]

    def quick_sort(self, array):
        """
        Sorts the given list using the quick sort algorithm.
        """
        length = len(array)
        self.__quick_sort_helper(array, 0, length - 1)

    def __quick_sort_helper(self, array, low, high):
        if low < high:
            pivot = self.__partition(array, low, high)
            self.__quick_sort_helper(array, low, pivot - 1)
            self.__quick_sort_helper(array, pivot + 1, high)

    def __partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def merge_sort(self, array):
        """
        Sorts the given list using the merge sort algorithm.
        """
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def heap_sort(self, array):
        """
        Sorts the given list using the heap sort algorithm.
        """
        length = len(array)
        for i in range(length // 2 - 1, -1, -1):
            self.__heapify(array, length, i)
        for i in range(length - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.__heapify(array, i, 0)

    def __heapify(self, array, length, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < length and array[left] > array[largest]:
            largest = left
        if right < length and array[right] > array[largest]:
            largest = right
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            self.__heapify(array, length, largest)

    def radix_sort(self, array):
        """
        Sorts the given list using the radix sort algorithm.
        """
        max_value = max(array)
        exp = 1
        while max_value / exp > 0:
            self.__counting_sort(array, exp)
            exp *= 10

    def __counting_sort(self, array, exp):
        length = len(array)
        result = [0] * length
        count = [0] * 10
        for i in range(0, length):
            index = (array[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = length - 1
        while i >= 0:
            index = (array[i] // exp) % 10
            result[count[index] - 1] = array[i]
            count[index] -= 1
            i -= 1
        for i in range(0, length):
            array[i] = result[i]

    def shell_sort(self, array):
        """
        Sorts the given list using the shell sort algorithm.
        """
        length = len(array)
        gap = 1
        while gap < length // 3:
            gap = 3 * gap + 1
        while gap > 0:
            for i in range(gap, length):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 3