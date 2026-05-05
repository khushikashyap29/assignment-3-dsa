def heapify(arr, n, i):
    largest = i       # root
    left = 2 * i + 1  # left child
    right = 2 * i + 2 # right child

    # check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if root is not largest, swap and heapify again
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # swap root (max) with last element
        arr[i], arr[0] = arr[0], arr[i]

        # call heapify on reduced heap
        heapify(arr, i, 0)


# ---- Main Program ----
arr = list(map(int, input("Enter elements separated by space: ").split()))

heap_sort(arr)

print("Sorted List:", arr)