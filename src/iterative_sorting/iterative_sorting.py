# TO-DO: Complete the selection_sort() function below
selected_arr = []


def selection_sort(arr):
    # loop through n-1 elements
    while arr[0] != min(arr) and arr[len(arr) - 1] != max(arr) or arr[0] == min(arr) and arr[len(arr) - 1] != max(arr) or arr[0] != min(arr) and arr[len(arr) - 1] == max(arr):
        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
            rh_side = arr[smallest_index:len(arr)]
            if len(rh_side) != 0:
                small_value = min(rh_side)
                arr.remove(small_value)
                arr.insert(smallest_index, small_value)
        print(arr)
        return arr
selection_sort([25, 67, 4, 33, 19])
selection_sort([33, 19, 150, 123, 167, 190])
selection_sort([234,4,34,56,78,97,0,45,6767,765453])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while arr[0] != min(arr) and arr[len(arr) - 1] != max(arr) or arr[0] == min(arr) and arr[len(arr) - 1] != max(arr) or arr[0] != min(arr) and arr[len(arr) - 1] == max(arr):
        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
            next_index = cur_index + 1
            if arr[smallest_index] >= arr[next_index]:
                add_item = arr[next_index]
                arr.remove(arr[next_index])
                arr.insert(smallest_index, add_item)  
            else:
                if arr[smallest_index] <= arr[next_index]:
                    add_item = arr[smallest_index]
                    arr.remove(arr[smallest_index])
                    arr.insert(smallest_index, add_item)
    print(arr)
    return arr


bubble_sort([25, 67, 4, 33, 19, 40, 190, 200, 1])


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
