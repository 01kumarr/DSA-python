'''
Delete midle element in an array or stack using recursing
'''

def delete_middle(arr:list, mid:int, k:int):
    if not arr:
        return arr 

    if k == mid:
        arr.pop(k)
        return 
    delete_middle(arr, mid, k+1)


array = [1,2,3,4,5]
delete_middle(array, 2, 0)
print(array)