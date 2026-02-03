import numpy as np
import time

def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[(low + high) // 2]
            i, j = low - 1, high + 1
            while True:
                i += 1
                while arr[i] < pivot: i += 1
                j -= 1
                while arr[j] > pivot: j -= 1
                if i >= j:
                    p = j
                    break
                arr[i], arr[j] = arr[j], arr[i]
            stack.append((low, p))
            stack.append((p + 1, high))

def main():
    data = np.load('data.npz')

    times = []
    for key in data.files:
        arr = data[key].copy()
        
        start = time.perf_counter()
        quick_sort(arr)
        end = time.perf_counter()
        
        ms = (end - start) * 1000
        times.append(ms)
        print(f"{key:<15} | {ms:>12.2f} ms")

    avg_time = sum(times) / len(times)
    print("-" * 35)
    print(f"{'Trung bình':<15} | {avg_time:>12.2f} ms")

if __name__ == "__main__":
    main()