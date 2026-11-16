'''
sortig an array using recursion : this is called divide and conqore : recursively devide the array into small
array and then merge them
'''


def sort_array(array:list):
    if len(array) <= 1:
        return array

    mid = len(array) // 2 
    left = sort_array(array[:mid]) 
    right = sort_array(array[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1

        k+=1

    while i < len(left):
        array[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        array[k] = right[j]
        j+=1
        k+=1

    return array 

# print(sort_array([3,4,1,8,6,7]))


# another approach : only recusion with hypothesis that calling function on smaller array

def helper(sorted_list, item):
    if not sorted_list or item <= sorted_list[0]:
        return [item] + sorted_list
     
    return [sorted_list[0]] + helper(sorted_list[1:], item)

def sort_array_recursion(array:list):
    if len(array) <= 1:
        return array 

    sorted_array = sort_array_recursion(array[1:])

    return helper(sorted_array, array[0])

print(sort_array_recursion([5,6,3,1,8]))