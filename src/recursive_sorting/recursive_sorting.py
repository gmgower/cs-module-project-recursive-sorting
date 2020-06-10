# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # Your code here
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    merged_arr += arrA[a:]
    merged_arr += arrB[b:]
    return merged_arr
    
merge([1,2,3], [4, 5, 6])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) > 1:
        arrA = merge_sort(arr[:len(arr) // 2])
        pass



    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
