import numpy as np
import time

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    stack = np.empty((n, 2), dtype=int)
    top = 0 
    
    stack[top, 0] = 0
    stack[top, 1] = n - 1
    
    while top >= 0:
        low = stack[top, 0]
        high = stack[top, 1]
        top -= 1 
        
        if low < high:
            pivot = arr[(low + high) // 2]
            i = low - 1
            j = high + 1
            
            while True:
                i += 1
                while arr[i] < pivot: i += 1
                
                j -= 1
                while arr[j] > pivot: j -= 1
                
                if i >= j:
                    p = j
                    break
                    
                arr[i], arr[j] = arr[j], arr[i]
            
            top += 1
            stack[top, 0] = low
            stack[top, 1] = p
            
            top += 1
            stack[top, 0] = p + 1
            stack[top, 1] = high

def main():
    data = np.load('data.npz')
    keys = data.files
    
    times = np.zeros(len(keys))
    
    for i, key in enumerate(keys):
        arr = data[key].copy()
        
        start = time.perf_counter()
        quick_sort(arr)
        end = time.perf_counter()
        
        ms = (end - start) * 1000
        times[i] = ms
        print(f"{key:<15} | {ms:>12.2f} ms")

    avg_time = np.mean(times)
    print("-" * 35)
    print(f"{'Trung bình':<15} | {avg_time:>12.2f} ms")

if __name__ == "__main__":
    main()
