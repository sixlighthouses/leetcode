# given a sorted array of integers find the index of target integer
# for example sorted array [-1, 3, 5, 6, 9, 11, 27] what index is 9 at
# should return 4 if it does not exist return -1

def find_target(source_array, target):
    left_index, right_index = 0, len(source_array) - 1

    while left_index  < right_index:
        mid_point = (left_index + right_index)//2
        if source_array[mid_point] < target:
            left_index = mid_point
        elif source_array[mid_point] > target:
            right_index = mid_point
        else:
            return mid_point

    return -1



source_array = [-1, 2, 3, 4, 9, 27, 38]
target = 9

result = find_target(source_array, target)
print(f"Target {target} found at index {result}")



