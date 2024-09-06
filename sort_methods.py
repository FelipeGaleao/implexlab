def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        L = arr[:meio]
        R = arr[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def heapify(arr, n, i):
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[maior] < arr[l]:
        maior = l

    if r < n and arr[maior] < arr[r]:
        maior = r

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def partition(arr, low, high):
    i = (low - 1)
    pivo = arr[high]

    for j in range(low, high):
        if arr[j] <= pivo:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def counting_sort(arr, max_val):
    m = max_val + 1
    contagem = [0] * m                
    
    for a in arr:
        contagem[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(contagem[a]): 
            arr[i] = a
            i += 1
    return arr


# vetor1 = [12, 5, 7, 3, 8, 10, 2]
# vetor2 = [15, 3, 2, 7, 9, 8, 4]
# vetor3 = [35, 12, 48, 23, 9, 56]
# vetor4 = [105, 203, 501, 304, 150, 401]
# vetor5 = [12, 31, 27, 100, 42, 89]

# #insertion sort 
# print(insertion_sort(vetor1))
# print(insertion_sort(vetor2))
# print(insertion_sort(vetor3))
# print(insertion_sort(vetor4))
# print(insertion_sort(vetor5))

# #merge sort
# print(merge_sort(vetor1))
# print(merge_sort(vetor2))
# print(merge_sort(vetor3))
# print(merge_sort(vetor4))
# print(merge_sort(vetor5))

# #Heap sort
# print(heap_sort(vetor1))
# print(heap_sort(vetor2))
# print(heap_sort(vetor3))
# print(heap_sort(vetor4))
# print(heap_sort(vetor5))

# #quick sort
# print(quick_sort(vetor1, 0, len(vetor1) - 1))
# print(quick_sort(vetor2, 0, len(vetor2) - 1))
# print(quick_sort(vetor3, 0, len(vetor3) - 1))
# print(quick_sort(vetor4, 0, len(vetor4) - 1))
# print(quick_sort(vetor5, 0, len(vetor5) - 1))

# #counting sort
