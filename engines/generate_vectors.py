from random import randint


class GenerateVectors():
    """ Classe utilizada para gerar vetores de inteiros aleatórios.
    """

    def __init__(self):
        pass

    def random(self, inc: int, fim: int, stp: int):
        """ Método que gera um vetor de inteiros aleatórios.

        Args:
            inc (int): Valor inicial do intervalo.
            fim (int): Valor final do intervalo.
            stp (int): Tamanho do vetor.

        Returns:
            list: Vetor de inteiros aleatórios.
        """
        return [randint(inc, fim) for _ in range(stp)]

    def reverse(self, increment: int, end: int, step: int):
        """ Método que gera um vetor de inteiros ordenados de forma decrescente. 

        Args:
            increment (int): Valor inicial do intervalo.
            end (int): Valor final do intervalo.
            step (int): Tamanho do vetor.

        Returns:
            list: Vetor de inteiros ordenados de forma decrescente.
        """
        return [i for i in range(end, increment, -1)]

    def ordered(self, increment: int, end: int, step: int):
        """ Método que gera um vetor de inteiros ordenados de forma crescente.

        Args:
            increment (int): Valor inicial do intervalo.
            end (int): Valor final do intervalo.
            step (int): Tamanho do vetor.
        """
        return [i for i in range(increment, end, step)]

    def almost_ordered(self, increment: int, end: int, step: int):
        """ Método que gera um vetor de inteiros quase ordenados.

        Args:
            increment (int): Valor inicial do intervalo.
            end (int): Valor final do intervalo.
            step (int): Tamanho do vetor.
        """
        vector = [i for i in range(increment, end, step)]
        vector[-1], vector[-2] = vector[-2], vector[-1]
        return vector
