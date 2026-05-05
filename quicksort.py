def partition(arr, low, high):
    pivot = arr[high]   # last element as pivot
    i = low - 1         # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # partition index
        pi = partition(arr, low, high)

        # sort left and right parts
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ---- Main Program ----
arr = list(map(int, input("Enter elements separated by space: ").split()))

quick_sort(arr, 0, len(arr) - 1)

print("Sorted List:", arr)