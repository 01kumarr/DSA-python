from collections import Counter
def get_good_substring(string: str, k: int) -> int:
    if k > len(string) or k <= 0:
        return 0
    if k == 1:
        return len(string)

    count = 0
    window_count = Counter(string[:k])
    
    if len(window_count) == k:
        count += 1

    for i in range(k, len(string)):
        right_char = string[i]
        window_count[right_char] += 1
        
        left_char = string[i - k]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
            
        if len(window_count) == k:
            count += 1

    return count

def get_good_substring(string: str, k: int) -> int:
    if k > len(string) or k <= 0:
        return 0
    if k == 1:
        return len(string)

    count = 0
    freq = [0] * 26  # Frequency array for 'a' through 'z'
    unique_count = 0

    # Initialize the first window of size k
    for i in range(k):
        idx = ord(string[i]) - ord('a')
        if freq[idx] == 0:
            unique_count += 1
        freq[idx] += 1

    if unique_count == k:
        count += 1

    # Slide the window across the rest of the string
    for i in range(k, len(string)):
        # Add the new character entering the window on the right
        right_idx = ord(string[i]) - ord('a')
        if freq[right_idx] == 0:
            unique_count += 1
        freq[right_idx] += 1

        # Remove the old character leaving the window on the left
        left_idx = ord(string[i - k]) - ord('a')
        freq[left_idx] -= 1
        if freq[left_idx] == 0:
            unique_count -= 1

        # Check if all characters in the current window are unique
        if unique_count == k:
            count += 1

    return count


import math
def get_min_window_sum(arr: list, target: int) -> int:
    if not arr:
        return 0
        
    min_window = math.inf
    window_sum = 0
    start = 0
    
    for end in range(len(arr)):
        window_sum += arr[end]

        while window_sum >= target:
            min_window = min(min_window, end - start + 1)
            window_sum -= arr[start]
            start += 1
            
    return min_window if min_window is not math.inf else 0
        
