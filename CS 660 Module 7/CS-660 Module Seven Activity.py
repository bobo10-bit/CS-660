import time
import tracemalloc
import random


# Quick Sort
def quick_sort(arr):
    # if there is more than one elements continue sorting
    if len(arr) <= 1:
        return arr

    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]

    # Create left side for every number smaller than the pivot 
    left = [x for x in arr if x < pivot]
    # Create middle side for every number equal to the pivot
    middle = [x for x in arr if x == pivot]
    # Create right side for every number greater than the pivot
    right = [x for x in arr if x > pivot]

    # Sorts the left and right side recursively and combines them with the middle side
    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort
def merge_sort(arr):
    # Is there is more than one element continue sorting
    if len(arr) <= 1:
        return arr
    # Finds where to split the list
    middle = len(arr) // 2

    # Sorts the left and right side recursively
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # Merge the sorted left and right sides and keep track of their positions
    result = []
    i = 0
    j = 0

    # compare elements until one of the lists are empty
    while i < len(left) and j < len(right):
        # If the left elements is smaller  add it
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # otherwise add the right element
        else:
            result.append(right[j])
            j += 1

    # Once a list is empty add the remaining elements from the other list
    result += left[i:]
    result += right[j:]

    # return the sorted list
    return result


# Heap Sort
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    # Assume the current element is the largest
    largest = i
    # Calculate the indices of the left and right children
    left = 2 * i + 1
    right = 2 * i + 2

    # if the left child is larger than the current largest element largest is changed to the left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    # if the right child is larger than the current largest element largest is changed to the right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If one of the children is larger than the current largest element swap them with the current element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Benchmarking function
def benchmark(sort_function, data, iterations=5):
    total_time = 0
    peak_memory = 0

    # runs for each iteration
    for i in range(iterations):
        # Makes a copy of the data
        test_data = data.copy()
        # Start the memory tracking
        tracemalloc.start()
        # Start the timer
        start = time.perf_counter()
        # Call the sorting function
        sort_function(test_data)
        # stop the timer
        end = time.perf_counter()
        # Get memory usage
        current, peak = tracemalloc.get_traced_memory()
        # Stop tracking memory
        tracemalloc.stop()
        # add the time
        total_time += end - start
        # keeps the highest memory usage
        if peak > peak_memory:
            peak_memory = peak
    # calculate average time and convert peak memory to MB
    average_time = total_time / iterations
    peak_memory_mb = peak_memory / (1024 * 1024)
    # Print results
    print("Algorithm:", sort_function.__name__)
    print("Average Time:", round(average_time * 1000, 2), "ms")
    print("Peak Memory:", round(peak_memory_mb, 5), "MB")
    print()


# Create 100,000 random integers
data = [random.randint(1, 1000000) for i in range(100000)]

# Run benchmarks
benchmark(quick_sort, data)
benchmark(merge_sort, data)
benchmark(heap_sort, data)