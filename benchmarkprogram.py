import random
import time

# ---------------- SORTING ALGORITHMS ---------------- #

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    arr = arr.copy()
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------------- DATASET GENERATION ---------------- #

def generate_data(n, data_type):
    if data_type == "random":
        return [random.randint(1, 10000) for _ in range(n)]
    elif data_type == "sorted":
        return list(range(n))
    elif data_type == "reverse":
        return list(range(n, 0, -1))


# ---------------- TIMING FUNCTION ---------------- #

def measure_time(func, arr):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return round(end - start, 6)


# ---------------- MAIN BENCHMARK ---------------- #

sizes = [1000, 5000, 10000]
types = ["random", "sorted", "reverse"]

seed = int(input("Enter seed value: "))
random.seed(seed)

print("\n--- Timing Table (seconds) ---")
print("Size\tType\t\tInsertion\tMerge\t\tQuick")

for size in sizes:
    for t in types:
        data = generate_data(size, t)

        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data)

        print(f"{size}\t{t}\t\t{t1}\t\t{t2}\t\t{t3}")