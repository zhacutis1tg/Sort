import numpy as np
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

def main():
    data = np.load('data.npz')

    times = []
    for key in data.files:
        arr = data[key].tolist()
        
        start = time.perf_counter()
        sorted_arr = merge_sort(arr)
        end = time.perf_counter()
        
        ms = (end - start) * 1000
        times.append(ms)
        print(f"{key:<15} | {ms:>12.2f} ms")

    avg_time = sum(times) / len(times)
    print("-" * 35)
    print(f"{'Trung bình':<15} | {avg_time:>12.2f} ms")

if __name__ == "__main__":
    main()