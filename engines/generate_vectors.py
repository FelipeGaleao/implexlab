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

    def reverse(self, inc: int, fim: int, stp: int):
        """ Método que gera um vetor de inteiros ordenados de forma decrescente. 

        Args:
            increment (int): Valor inicial do intervalo.
            end (int): Valor final do intervalo.
            step (int): Tamanho do vetor.

        Returns:
            list: Vetor de inteiros ordenados de forma decrescente.
        """
        vetor_generate = [i for i in range(inc, fim, stp)]
        vetor_generate = vetor_generate[::-1]
        return vetor_generate
        
    def ordered(self, increment: int, end: int, step: int):
        """ Método que gera um vetor de inteiros ordenados de forma crescente.

        Args:
            increment (int): Valor inicial do intervalo.
            end (int): Valor final do intervalo.
            step (int): Tamanho do vetor.
        """
        return [i for i in range(increment, end, step)]

    def almost_ordered(self, increment: int, end: int, step: int):
        """ Método que gera um vetor de inteiros quase ordenados (10% dos elementos estão fora de ordem).

        Args:
            increment (int): Valor inicial do intervalo.
            end (int): Valor final do intervalo.
            step (int): Tamanho do vetor.
        """
        vetor_generate = self.ordered(increment, end, step)
        for i in range(int(len(vetor_generate)*0.1)):
            index = randint(0, len(vetor_generate)-1)
            vetor_generate[index] = randint(increment, end)
        return vetor_generate
