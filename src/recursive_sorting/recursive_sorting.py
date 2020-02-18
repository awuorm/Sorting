# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    merging_arr = []
    sorted  = True
    while sorted:
        sorted  = False
        for mergeitem in range(len(merged_arr)-1):
            for item in range(len(arrA)-1):
                if arrA[item] > arrA[item+1]:
                    arrA[item],arrA[item+1] = arrA[item+1],arrA[item]
                    sorted  = True
            for itemb in range(len(arrB)-1):
                if arrB[itemb] > arrB[itemb+1]:
                    arrB[itemb],arrB[itemb+1] = arrB[itemb+1],arrB[itemb]
                    sorted  = True
                    merging_arr = arrA + arrB
                    print(f'the arrays {merging_arr}')
                if merging_arr[mergeitem] >= merging_arr[mergeitem +1]:
                    merging_arr[mergeitem],merging_arr[mergeitem+1] = merging_arr[mergeitem+1],merging_arr[mergeitem]
                    # print(f"it works {merging_arr}")
                    sorted = True
    merged_arr = merging_arr
    print(f"{merged_arr}")
        # TO-DO
    return merged_arr
merge([3,7,6,5],[8,1,4,2])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0 or len(arr) == 1 :
        return arr
    else:
        # print(len(arr)//2)
        # print(arr[0:len(arr)//2],arr[len(arr)//2:len(arr)])
        return merge(arr[0:len(arr)//2],arr[len(arr)//2:len(arr)])
    return arr
merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
