def binary_search_with_iterations(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            upper_bound = arr[mid]

    # If target is greater than all elements
    if upper_bound is None and arr and target > arr[-1]:
        upper_bound = float('inf')

    return iterations, upper_bound


if __name__ == '__main__':
    examples = [
        ([1.1, 2.2, 3.3, 4.4, 5.5], 3.3),
        ([1.1, 2.2, 3.3, 4.4, 5.5], 4.0),
        ([1.1, 2.2, 3.3, 4.4, 5.5], 12.0),
    ]

    for array, target in examples:
        result = binary_search_with_iterations(array, target)
        print(f"Find {target} in {array}: {result}")
