from engines.sort_engines import BubbleSort, QuickSort, MergeSort, HeapSort, InsertionSort, CountingSort
from engines.generate_vectors import GenerateVectors

inc = int(input("Enter the start of the range: "))
fim = int(input("Enter the end of the range: "))
stp = int(input("Enter the step: "))

DECIMAL_PLACES = 3

generate_vector = GenerateVectors()
bubble_sort = BubbleSort()
quick_sort = QuickSort()
merge_sort = MergeSort()
heap_sort = HeapSort()
insertion_sort = InsertionSort()
counting_sort = CountingSort()


random = generate_vector.random(inc, fim, stp)
reverse = generate_vector.reverse(inc, fim, stp)
ordered = generate_vector.ordered(inc, fim, stp)

file_results = open("results.txt", "w")
file_results.write(
    "MODE, N, BUBBLE, QUICK, MERGE, HEAP, INSERTION, COUNTING\n")

print("[[RANDOM]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "QuickSort", "\t"*2,
      "MergeSort", "\t"*2, "HeapSort", "\t"*2, "InsertionSort", "\t"*2, "Couting")
for i in range(0, fim+stp, stp):
    if i == 0:
        continue
    vetor = generate_vector.random(inc, i, stp)

    vetor_bubble = vetor.copy()
    vetor_quick = vetor.copy()
    vetor_merge = vetor.copy()
    vetor_heap = vetor.copy()
    vetor_insertion = vetor.copy()
    vetor_counting = vetor.copy()

    # Calculando o tempo de cada algoritmo
    bubble_duration = bubble_sort.sort(vetor_bubble)
    quick_duration = quick_sort.sort(vetor_quick)
    merge_sort_duration = merge_sort.sort(vetor_merge)
    heap_sort_duration = heap_sort.sort(vetor_heap)
    insertion_sort_duration = insertion_sort.sort(vetor_insertion)
    counting_sort_duration = counting_sort.sort(vetor_counting)
    print("\t"*2, i, "\t"*2, bubble_duration, DECIMAL_PLACES), "\t"*3, round(insertion_sort_duration, DECIMAL_PLACES), "\t"*3, round(merge_sort_duration,
                                                                                                                                     DECIMAL_PLACES), "\t"*3, round(heap_sort_duration, DECIMAL_PLACES), "\t"*3, round(quick_duration, DECIMAL_PLACES), "\t"*3, round(counting_sort_duration, DECIMAL_PLACES)
    file_results.write("RANDOM, {}, {}, {}, {}, {}, {}, {}\n".format(i, bubble_duration, quick_duration,
                       merge_sort_duration, heap_sort_duration, insertion_sort_duration, counting_sort_duration))

print("[[REVERSE]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "QuickSort", "\t"*2,
      "MergeSort", "\t"*2, "HeapSort", "\t"*2, "InsertionSort", "\t"*2, "Couting")

for i in range(0, fim+stp, stp):
    if i == 0:
        continue
    if i == inc:
        pass
    vetor = generate_vector.reverse(inc, i, stp)
    vetor_bubble = vetor.copy()
    vetor_quick = vetor.copy()
    vetor_merge = vetor.copy()
    vetor_heap = vetor.copy()
    vetor_insertion = vetor.copy()
    vetor_counting = vetor.copy()

    # Calculando o tempo de cada algoritmo
    bubble_duration = bubble_sort.sort(vetor_bubble)
    quick_duration = quick_sort.sort(vetor_quick)
    merge_sort_duration = merge_sort.sort(vetor_merge)
    heap_sort_duration = heap_sort.sort(vetor_heap)
    insertion_sort_duration = insertion_sort.sort(vetor_insertion)
    counting_sort_duration = 0
    print("\t"*2, i, "\t"*2, round(bubble_duration, DECIMAL_PLACES), "\t"*3, round(insertion_sort_duration, DECIMAL_PLACES), "\t"*3, round(merge_sort_duration, DECIMAL_PLACES),
          "\t"*3, round(heap_sort_duration, DECIMAL_PLACES), "\t"*3, round(quick_duration, DECIMAL_PLACES), "\t"*3, round(counting_sort_duration, DECIMAL_PLACES))
    file_results.write("REVERSE, {}, {}, {}, {}, {}, {}, {}\n".format(i, bubble_duration, quick_duration,
                       merge_sort_duration, heap_sort_duration, insertion_sort_duration, counting_sort_duration))

print("[[ORDERED]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "QuickSort", "\t"*2,
      "MergeSort", "\t"*2, "HeapSort", "\t"*2, "InsertionSort", "\t"*2, "Couting")
for i in range(0, fim+stp, stp):
    if i == 0:
        continue
    vetor = generate_vector.ordered(inc, i, stp)
    vetor_bubble = vetor.copy()
    vetor_quick = vetor.copy()
    vetor_merge = vetor.copy()
    vetor_heap = vetor.copy()
    vetor_insertion = vetor.copy()
    vetor_counting = vetor.copy()

    # Calculando o tempo de cada algoritmo
    bubble_duration = bubble_sort.sort(vetor_bubble)
    quick_duration = quick_sort.sort(vetor_quick)
    merge_sort_duration = merge_sort.sort(vetor_merge)
    heap_sort_duration = heap_sort.sort(vetor_heap)
    insertion_sort_duration = insertion_sort.sort(vetor_insertion)
    counting_sort_duration = 0
    print("\t"*2, i, "\t"*2, round(bubble_duration, DECIMAL_PLACES), "\t"*3, round(insertion_sort_duration, DECIMAL_PLACES), "\t"*3, round(merge_sort_duration, DECIMAL_PLACES),
          "\t"*3, round(heap_sort_duration, DECIMAL_PLACES), "\t"*3, round(quick_duration, DECIMAL_PLACES), "\t"*3, round(counting_sort_duration, DECIMAL_PLACES))
    file_results.write("ORDERED, {}, {}, {}, {}, {}, {}, {}\n".format(i, bubble_duration, quick_duration,
                       merge_sort_duration, heap_sort_duration, insertion_sort_duration, counting_sort_duration))

print("[[ALMOST ORDERED]]")
print("\t"*2, "n", "\t"*2, "BubbleSort", "\t"*2, "QuickSort", "\t"*2,
      "MergeSort", "\t"*2, "HeapSort", "\t"*2, "InsertionSort", "\t"*2, "Couting")

for i in range(0, fim+stp, stp):
    if i == 0:
        continue
    if i == inc:
        pass
    vetor = generate_vector.almost_ordered(inc, i, stp)
    vetor_bubble = vetor.copy()
    vetor_quick = vetor.copy()
    vetor_merge = vetor.copy()
    vetor_heap = vetor.copy()
    vetor_insertion = vetor.copy()
    vetor_counting = vetor.copy()

    # Calculando o tempo de cada algoritmo
    bubble_duration = bubble_sort.sort(vetor_bubble)
    quick_duration = quick_sort.sort(vetor_quick)
    merge_sort_duration = merge_sort.sort(vetor_merge)
    heap_sort_duration = heap_sort.sort(vetor_heap)
    insertion_sort_duration = insertion_sort.sort(vetor_insertion)
    counting_sort_duration = 0
    print("\t"*2, i, "\t"*2, round(bubble_duration, DECIMAL_PLACES), "\t"*3, round(insertion_sort_duration, DECIMAL_PLACES), "\t"*3, round(merge_sort_duration, DECIMAL_PLACES),
          "\t"*3, round(heap_sort_duration, DECIMAL_PLACES), "\t"*3, round(quick_duration, DECIMAL_PLACES), "\t"*3, round(counting_sort_duration, DECIMAL_PLACES))
    file_results.write("ALMOST_ORDERED, {}, {}, {}, {}, {}, {}, {}\n".format(i, bubble_duration, quick_duration,
                       merge_sort_duration, heap_sort_duration, insertion_sort_duration, counting_sort_duration))
