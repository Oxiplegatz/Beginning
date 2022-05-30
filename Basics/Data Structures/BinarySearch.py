def binary_search(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "value not found"

    # We calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # we reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # we reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))


# Iterative Approach
def binary_search(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)

    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            right_pointer = mid_idx
        if target > mid_val:
            left_pointer = mid_idx + 1

    return "Value not in list"


# test cases
print(binary_search([5, 6, 7, 8, 9], 9))
print(binary_search([5, 6, 7, 8, 9], 10))
print(binary_search([5, 6, 7, 8, 9], 8))
print(binary_search([5, 6, 7, 8, 9], 4))
print(binary_search([5, 6, 7, 8, 9], 6))
