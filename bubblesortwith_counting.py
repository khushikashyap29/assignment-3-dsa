def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1   # count comparison

            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1      # count swap

    return arr, comparisons, swaps


# ---- Input ----
arr = list(map(int, input("Enter elements separated by space: ").split()))

# ---- Function Call ----
sorted_arr, comp, swp = bubble_sort(arr)

# ---- Output ----
print("Sorted List:", sorted_arr)
print("Total Comparisons:", comp)
print("Total Swaps:", swp)