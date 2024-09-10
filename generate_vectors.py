from random import randint
import random 

def random_vector(inc: int, fim: int, stp: int):
    """ Gera um vetor de inteiros aleatórios.

    Args:
        inc (int): Valor inicial do intervalo.
        fim (int): Valor final do intervalo.
        stp (int): Tamanho do vetor.

    Returns:
        list: Vetor de inteiros aleatórios.
    """
    return [randint(inc, fim) for _ in range(stp)]

def reverse_vector(increment: int, end: int, step: int):
    """ Gera um vetor de inteiros ordenados de forma decrescente.

    Args:
        increment (int): Valor inicial do intervalo.
        end (int): Valor final do intervalo.
        step (int): Tamanho do vetor.

    Returns:
        list: Vetor de inteiros ordenados de forma decrescente.
    """
    return [i for i in range(end, increment, -1)]

def ordered_vector(increment: int, end: int, step: int):
    """ Gera um vetor de inteiros ordenados de forma crescente.

    Args:
        increment (int): Valor inicial do intervalo.
        end (int): Valor final do intervalo.
        step (int): Tamanho do vetor.
    """
    return [i for i in range(increment, end, step)]

def almost_ordered_vector(increment: int, end: int, step: int):
    """ Gera um vetor de inteiros quase ordenados.

    Args:
        increment (int): Valor inicial do intervalo.
        end (int): Valor final do intervalo.
        step (int): Tamanho do vetor.
    """
    # vetor ordenado crescente
    vector = [i for i in range(increment, end, step)]
    
    # Verificar se o vetor não está vazio
    if not vector:
        return vector
    
    # Calcular o número de elementos a serem embaralhados (10% do tamanho do vetor)
    num_elements_to_shuffle = max(1, len(vector) // 10)  # Garantir pelo menos 1 elemento para embaralhar

    # Embaralhar 10% dos elementos
    indices_to_shuffle = random.sample(range(len(vector)), num_elements_to_shuffle)
    elements_to_shuffle = [vector[i] for i in indices_to_shuffle]
    random.shuffle(elements_to_shuffle)
    
    # Substituir os elementos no vetor original pelos elementos embaralhados
    for index, original_index in enumerate(indices_to_shuffle):
        vector[original_index] = elements_to_shuffle[index]
    
    return vector