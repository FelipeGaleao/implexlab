import time
from generate_vectors import almost_ordered_vector, ordered_vector, random_vector, reverse_vector
from sort_methods import bubble_sort, counting_sort, heap_sort, insertion_sort, merge_sort, quick_sort


inc = int(input("Enter the start of the range: "))
fim = int(input("Enter the end of the range: "))
stp = int(input("Enter the step: "))

print("[[RANDOM]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "InsertionSort", "\t"*2, "MergeSort", "\t"*2, "HeapSort", "\t"*2, "QuickSort", "\t"*2, "CountingSort")
for i in range(0, fim, stp):
    if i == 0:
        continue
    try:
        vetor = random_vector(inc, i, stp)
        print("\t"*2, i, "\t"*2, end="")
        # BubbleSort
        bubble_start = time.time()
        bubble_sort(vetor.copy())
        bubble_duration = round(time.time() - bubble_start, 4)
        print(bubble_duration, "\t"*2, end="")

        # InsertionSort
        insertion_start = time.time()
        insertion_sort(vetor.copy())
        insertion_duration = round(time.time() - insertion_start, 4)
        print(insertion_duration, "\t"*2, end="")

        # MergeSort
        merge_start = time.time()
        merge_sort(vetor.copy())
        merge_duration = round(time.time() - merge_start, 4)
        print(merge_duration, "\t"*2, end="")

        # HeapSort
        heap_start = time.time()
        heap_sort(vetor.copy())
        heap_duration = round(time.time() - heap_start, 4)
        print(heap_duration, "\t"*2, end="")

        # QuickSort
        quick_start = time.time()
        quick_sort(vetor.copy(), 0, len(vetor) - 1)
        quick_duration = round(time.time() - quick_start, 4)
        print(quick_duration, "\t"*2, end="")

        # CountingSort
        counting_start = time.time()
        max_val = max(vetor)
        counting_sort(vetor.copy(), max_val)
        counting_duration = round(time.time() - counting_start, 4)
        print(counting_duration)
    except ValueError as e:
        print(f"Error: {e}")

print("[[REVERSE]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "InsertionSort", "\t"*2, "MergeSort", "\t"*2, "HeapSort", "\t"*2, "QuickSort", "\t"*2, "CountingSort")
for i in range(0, fim, stp):
    if i == 0:
        continue
    try:
        vetor = reverse_vector(inc, i, stp)
        print("\t"*2, i, "\t"*2, end="")
        # BubbleSort
        bubble_start = time.time()
        bubble_sort(vetor.copy())
        bubble_duration = round(time.time() - bubble_start, 4)
        print(bubble_duration, "\t"*2, end="")

        # InsertionSort
        insertion_start = time.time()
        insertion_sort(vetor.copy())
        insertion_duration = round(time.time() - insertion_start, 4)
        print(insertion_duration, "\t"*2, end="")

        # MergeSort
        merge_start = time.time()
        merge_sort(vetor.copy())
        merge_duration = round(time.time() - merge_start, 4)
        print(merge_duration, "\t"*2, end="")

        # HeapSort
        heap_start = time.time()
        heap_sort(vetor.copy())
        heap_duration = round(time.time() - heap_start, 4)
        print(heap_duration, "\t"*2, end="")

        # QuickSort
        quick_start = time.time()
        quick_sort(vetor.copy(), 0, len(vetor) - 1)
        quick_duration = round(time.time() - quick_start, 4)
        print(quick_duration, "\t"*2, end="")

        # CountingSort
        counting_start = time.time()
        max_val = max(vetor)
        counting_sort(vetor.copy(), max_val)
        counting_duration = round(time.time() - counting_start, 4)
        print(counting_duration)
    except ValueError as e:
        print(f"Error: {e}")

print("[[ORDERED]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "InsertionSort", "\t"*2, "MergeSort", "\t"*2, "HeapSort", "\t"*2, "QuickSort", "\t"*2, "CountingSort")
for i in range(0, fim, stp):
    if i == 0:
        continue
    try:
        vetor = ordered_vector(inc, i, stp)
        print("\t"*2, i, "\t"*2, end="")
        # BubbleSort
        bubble_start = time.time()
        bubble_sort(vetor.copy())
        bubble_duration = round(time.time() - bubble_start, 4)
        print(bubble_duration, "\t"*2, end="")

        # InsertionSort
        insertion_start = time.time()
        insertion_sort(vetor.copy())
        insertion_duration = round(time.time() - insertion_start, 4)
        print(insertion_duration, "\t"*2, end="")

        # MergeSort
        merge_start = time.time()
        merge_sort(vetor.copy())
        merge_duration = round(time.time() - merge_start, 4)
        print(merge_duration, "\t"*2, end="")

        # HeapSort
        heap_start = time.time()
        heap_sort(vetor.copy())
        heap_duration = round(time.time() - heap_start, 4)
        print(heap_duration, "\t"*2, end="")

        # QuickSort
        quick_start = time.time()
        quick_sort(vetor.copy(), 0, len(vetor) - 1)
        quick_duration = round(time.time() - quick_start, 4)
        print(quick_duration, "\t"*2, end="")

        # CountingSort
        counting_start = time.time()
        max_val = max(vetor)
        counting_sort(vetor.copy(), max_val)
        counting_duration = round(time.time() - counting_start, 4)
        print(counting_duration)
    except ValueError as e:
        print(f"Error: {e}")

print("[[ALMOST ORDERED]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "InsertionSort", "\t"*2, "MergeSort", "\t"*2, "HeapSort", "\t"*2, "QuickSort", "\t"*2, "CountingSort")
for i in range(0, fim, stp):
    if i == 0:
        continue
    try:
        vetor = almost_ordered_vector(inc, i, stp)
        print("\t"*2, i, "\t"*2, end="")
        # BubbleSort
        bubble_start = time.time()
        bubble_sort(vetor.copy())
        bubble_duration = round(time.time() - bubble_start, 4)
        print(bubble_duration, "\t"*2, end="")

        # InsertionSort
        insertion_start = time.time()
        insertion_sort(vetor.copy())
        insertion_duration = round(time.time() - insertion_start, 4)
        print(insertion_duration, "\t"*2, end="")

        # MergeSort
        merge_start = time.time()
        merge_sort(vetor.copy())
        merge_duration = round(time.time() - merge_start, 4)
        print(merge_duration, "\t"*2, end="")

        # HeapSort
        heap_start = time.time()
        heap_sort(vetor.copy())
        heap_duration = round(time.time() - heap_start, 4)
        print(heap_duration, "\t"*2, end="")

        # QuickSort
        quick_start = time.time()
        quick_sort(vetor.copy(), 0, len(vetor) - 1)
        quick_duration = round(time.time() - quick_start, 4)
        print(quick_duration, "\t"*2, end="")

        # CountingSort
        counting_start = time.time()
        max_val = max(vetor)
        counting_sort(vetor.copy(), max_val)
        counting_duration = round(time.time() - counting_start, 4)
        print(counting_duration)
    except ValueError as e:
        print(f"Error: {e}")