# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    if len(arr) == 0:
        return arr
    else:
        while len(arr) != 0 and arr[0] != min(arr) and arr[len(arr) - 1] != max(arr) or arr[0] == min(arr) and arr[len(arr) - 1] != max(arr) or arr[0] != min(arr) and arr[len(arr) - 1] == max(arr):
            for i in range(0, len(arr) - 1):
                cur_index = i
                smallest_index = cur_index
                rh_side = arr[smallest_index:len(arr)]
                if len(rh_side) != 0:
                    small_value = min(rh_side)
                    arr.remove(small_value)
                    arr.insert(smallest_index, small_value)
                    # arr[smallest_index],small_value = small_value,arr[smallest_index]

        # print(arr)
        return arr


selection_sort([25, 67, 4, 33, 19])
selection_sort([33, 19, 150, 123, 167, 190])
selection_sort([234, 4, 34, 56, 78, 97, 0, 45, 6767, 765453])
selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    sorted = True
    if len(arr) == 0:
        return arr
    else:
        while sorted:
            sorted = False
            for i in range(0, len(arr) - 1):
                cur_index = i
                smallest_index = cur_index
                next_index = cur_index + 1
                if arr[smallest_index] >= arr[next_index]:
                    arr[smallest_index], arr[next_index] = arr[next_index], arr[smallest_index]
                    sorted = True
        # print(arr)
        return arr


bubble_sort([25, 67, 4, 33, 19, 40, 190, 200, 1])


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#     actual_count = []
#     max_value = max(arr)
#     counted = 0
#     count = [0 for i in range(max_value + 1)]
#     # print(len(count))
#     for index in range(len(count)):
#         for item in arr:
#             # print(f" count before {counted},{item}")
#             if item == index:
#                 counted += 1
#                 count[index] = counted
#                 # print(f" count after {counted},{item}")
#             else:
#                 count[index] = counted
#     actual_count = [count[i]-count[i-1] if count[i] != 0 else count[i] for i in range(len(count))]
#     # print(actual_count)
#     counted_zeros = 0
#     counted_ones = 0
#     counted_morethanone = 0
#     for value_index in range(len(actual_count)):
#             if actual_count[value_index] == 0:
#                 print(f"value {actual_count[value_index]}")
#                 counted_zeros += 1
#             elif actual_count[value_index] == 1:
#                 print(f"value in one {value_index}")
#                 if value_index < len(arr):
#                 arr[value_index-] = value_index
#             elif actual_count[value_index] > 1:
#                 for x in range(1,value_index-1):
#                     arr[x] = value_index
#     # [0, 1, 2, 2, 1, 0, 0, 0, 1]
#     print(arr)
#     return arr
# # count_sort([1, 2, 3])
# count_sort([4, 2, 2, 8, 3, 3, 1])

def count_sort(array,maximum=-1):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        if output[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            array[i] = output[i]
    return array
data = [4, 2, 2, 8, 3, 3, 1]
count_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)

# if arrB[itemb] > arrA[itemb]:
#                     merged_arr[mergeitem] = arrA[itemb]
#                     sorted  = True
#                 else:
#                     merged_arr[mergeitem] = arr[itemb]
#                     sorted  = True
