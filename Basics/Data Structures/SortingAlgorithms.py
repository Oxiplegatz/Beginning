from random import randrange, shuffle


# Bubble Sort Algorithm

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Bubble Sort Algorithm Test:\n')
print("PRE SORT: {0}".format(nums))


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for el in arr:
        for index in range(len(arr) - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)

    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))
print('---------------------------------------------\n')


# Merge Sort Algorithm

def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


print('Merge Sort Algorithm Test:\n')

unordered_list = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595,
                  571, 268, 373]

ordered_list = merge_sort(unordered_list)

print(unordered_list)
print('\nSorted:\n')
print(ordered_list)
print('---------------------------------------------\n')


# Quicksort Algorithm

print('Quicksort Algorithm Test:\n')


def quicksort(a_list, start, end):
    # this portion of list has been sorted
    if start >= end:
        return
    print("Running quicksort on {0}".format(a_list[start: end + 1]))
    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = a_list[pivot_idx]
    print("Selected pivot {0}".format(pivot_element))
    # swap random element with last element in sub-lists
    a_list[end], a_list[pivot_idx] = a_list[pivot_idx], a_list[end]
    print('Pivot swapped with the last element:')
    print(a_list)

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if a_list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            print("Swapping {0} with {1}".format(a_list[i], pivot_element))
            a_list[i], a_list[less_than_pointer] = a_list[less_than_pointer], a_list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    a_list[end], a_list[less_than_pointer] = a_list[less_than_pointer], a_list[end]
    print("{0} successfully partitioned".format(a_list[start: end + 1]))
    # recursively sort left and right sub-lists
    quicksort(a_list, start, less_than_pointer - 1)
    quicksort(a_list, less_than_pointer + 1, end)


lst = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(lst)
print("PRE SORT: ", lst)
print(quicksort(lst, 0, len(lst) - 1))
print("POST SORT: ", lst)
