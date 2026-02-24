import numpy as np
import time

def heapify(arr, n, i):
    largest = i    
    l = 2 * i + 1    
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

def main():
    data = np.load('data.npz')
    keys = data.files
    
    times = np.zeros(len(keys)) 

    for i, key in enumerate(keys):
        arr = data[key].copy()
        
        start = time.perf_counter()
        heap_sort(arr)
        end = time.perf_counter()
        
        ms = (end - start) * 1000
        times[i] = ms
        print(f"{key:<15} | {ms:>12.2f} ms")

    avg_time = np.mean(times) 
    print("-" * 35)
    print(f"{'Trung bình':<15} | {avg_time:>12.2f} ms")

if __name__ == "__main__":

    main()
