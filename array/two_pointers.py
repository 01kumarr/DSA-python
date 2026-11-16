def find_max_sum(arr:list, k:int)->int:
    if k == 1:
        return max(arr) 

    max_sum = sum(arr[:k]) 

    for i in range(k, len(arr)):
        current_sum = max_sum + arr[i] - arr[i-k] 
        max_sum = max(max_sum, current_sum) 

    return max_sum
