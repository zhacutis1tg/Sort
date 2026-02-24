import numpy as np
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = np.empty(len(left) + len(right), dtype=left.dtype)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr[k] = left[i]
            i += 1
        else:
            sorted_arr[k] = right[j]
            j += 1
            
        k += 1
    
    if i < len(left):
        sorted_arr[k:] = left[i:]
    if j < len(right):
        sorted_arr[k:] = right[j:]
    
    return sorted_arr

def main():
    data = np.load('data.npz')
    keys = data.files
    
    times = np.zeros(len(keys))
    
    for idx, key in enumerate(keys):
        arr = data[key]
        
        start = time.perf_counter()
        sorted_arr = merge_sort(arr)
        end = time.perf_counter()
        
        ms = (end - start) * 1000
        times[idx] = ms
        print(f"{key:<15} | {ms:>12.2f} ms")

    avg_time = np.mean(times)
    print("-" * 35)
    print(f"{'Trung bình':<15} | {avg_time:>12.2f} ms")

if __name__ == "__main__":
    main()
