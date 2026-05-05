def insertion_sort(arr, show_pass=False):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        # Optional pass-wise printing
        if show_pass:
            print(f"Pass {i}: {arr}")

    return arr


# ---- Input ----
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Ask user if they want pass-wise output
choice = input("Show pass-wise output? (y/n): ")

# ---- Function Call ----
sorted_arr = insertion_sort(arr, choice.lower() == 'y')

# ---- Output ----
print("Sorted List:", sorted_arr)