import numpy as np
import time

data = np.load('data.npz')

times = []

for key in data.files:
    arr = data[key].copy()
    
    start = time.perf_counter()
    arr.sort() 
    end = time.perf_counter()
    
    ms = (end - start) * 1000
    times.append(ms)
    
    print(f"{key:<15} | {ms:>10.2f} ms")

avg_time = sum(times) / len(times)
print("-" * 35)
print(f"{'TRUNG BÌNH':<15} | {avg_time:>10.2f} ms")