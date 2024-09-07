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

    def sort(self, vector_to_sort: list):
        pass


class HeapSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação HeapSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list):
        pass


class InsertionSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação InsertionSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list):
        pass


class CountingSort(SortEngine):
    """Classe que implementa o algoritmo de ordenação CountingSort."""

    def __init__(self):
        super().__init__()

    def sort(self, vector_to_sort: list):
        pass
