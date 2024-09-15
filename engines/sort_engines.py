from abc import ABC, abstractmethod
from time import time


class SortEngine(ABC):
    """Classe base para implementação de métodos de ordenação que serão utilizados pelo trabalho."""

    def __init__(self):
        self.time = 0
        self.duration = None

    @abstractmethod
    def sort(self, vector_to_sort: list):
        pass

    def start_time(self):
        self.time = time()

    def end_time(self):
        self.duration = time() - self.time
        return self.duration


class BubbleSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação BubbleSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list) -> list:
        """Método que ordena um vetor utilizando o algoritmo BubbleSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.

        Returns:
            list: Vetor ordenado.
        """
        self.start_time()
        n = len(vector_to_sort)
        for i in range(n):
            for j in range(0, n - i - 1):
                if vector_to_sort[j] > vector_to_sort[j + 1]:
                    vector_to_sort[j], vector_to_sort[j +
                                                      1] = vector_to_sort[j + 1], vector_to_sort[j]
        duration = self.end_time()
        return duration


class QuickSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação QuickSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list) -> list:
        """Método que ordena um vetor utilizando o algoritmo QuickSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.

        Returns:
            list: Vetor ordenado.
        """
        self.start_time()
        self._quick_sort(vector_to_sort, 0, len(vector_to_sort) - 1)
        duration = self.end_time()
        return duration

    def _quick_sort(self, vector_to_sort: list, low: int, high: int):
        """Método que implementa o algoritmo QuickSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.
            low (int): O índice do primeiro elemento do vetor.
            high (int): O índice do último elemento do vetor.
        """
        if low < high:
            pivot_index = self._partition(vector_to_sort, low, high)
            self._quick_sort(vector_to_sort, low, pivot_index - 1)
            self._quick_sort(vector_to_sort, pivot_index + 1, high)

    def _partition(self, vector_to_sort: list, low: int, high: int) -> int:
        """O método que particiona o vetor e retorna o índice do pivô.

        Args:
            vector_to_sort (list): Vetor que será ordenado.
            low (int): Menor índice do vetor.
            high (int): Maior índice do vetor.

        Returns:
            int: O índice do pivô.
        """
        pivot = vector_to_sort[high]
        i = low - 1
        for j in range(low, high):
            if vector_to_sort[j] <= pivot:
                i += 1
                vector_to_sort[i], vector_to_sort[j] = vector_to_sort[j], vector_to_sort[i]
        vector_to_sort[i + 1], vector_to_sort[high] = vector_to_sort[high], vector_to_sort[i + 1]
        return i + 1


class MergeSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação MergeSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list) -> list:
        """Método que ordena um vetor utilizando o algoritmo MergeSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.

        Returns:
            list: Vetor ordenado.
        """
        self.start_time()
        self._merge_sort(vector_to_sort)
        duration = self.end_time()
        return duration

    def _merge_sort(self, vector: list) -> list:
        if len(vector) > 1:
            mid = len(vector) // 2
            left_half = vector[:mid]
            right_half = vector[mid:]

            self._merge_sort(left_half)
            self._merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    vector[k] = left_half[i]
                    i += 1
                else:
                    vector[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                vector[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                vector[k] = right_half[j]
                j += 1
                k += 1

        return vector


class HeapSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação HeapSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list) -> list:
        """Método que ordena um vetor utilizando o algoritmo HeapSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.

        Returns:
            list: Vetor ordenado.
        """
        self.start_time()
        self._heap_sort(vector_to_sort)
        duration = self.end_time()
        return duration

    def _heap_sort(self, vector: list):
        n = len(vector)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(vector, n, i)

        for i in range(n - 1, 0, -1):
            vector[i], vector[0] = vector[0], vector[i]
            self._heapify(vector, i, 0)

    def _heapify(self, vector: list, n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and vector[i] < vector[left]:
            largest = left

        if right < n and vector[largest] < vector[right]:
            largest = right

        if largest != i:
            vector[i], vector[largest] = vector[largest], vector[i]
            self._heapify(vector, n, largest)


class InsertionSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação InsertionSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list) -> list:
        """Método que ordena um vetor utilizando o algoritmo InsertionSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.

        Returns:
            list: Vetor ordenado.
        """
        self.start_time()
        self._insertion_sort(vector_to_sort)
        duration = self.end_time()
        return duration

    def _insertion_sort(self, vector: list):
        for i in range(1, len(vector)):
            key = vector[i]
            j = i - 1
            while j >= 0 and key < vector[j]:
                vector[j + 1] = vector[j]
                j -= 1
            vector[j + 1] = key


class CountingSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação CountingSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list) -> list:
        """Método que ordena um vetor utilizando o algoritmo CountingSort.

        Args:
            vector_to_sort (list): Vetor que será ordenado.

        Returns:
            list: Vetor ordenado.
        """
        self.start_time()
        self._counting_sort(vector_to_sort)
        duration = self.end_time()
        return duration

    def _counting_sort(self, vector: list) -> list:
        if len(vector) == 0 or vector is None:
            return 0
        max_val = max(vector)
        min_val = min(vector)
        range_of_elements = max_val - min_val + 1

        count = [0] * range_of_elements
        output = [0] * len(vector)

        for i in range(len(vector)):
            count[vector[i] - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for i in range(len(vector) - 1, -1, -1):
            output[count[vector[i] - min_val] - 1] = vector[i]
            count[vector[i] - min_val] -= 1

        for i in range(len(vector)):
            vector[i] = output[i]

        return vector
