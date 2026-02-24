import numpy as np
import time

data = np.load('data.npz')
keys = data.files

times = np.zeros(len(keys))

for i, key in enumerate(keys):
    arr = data[key].copy()
    
    start = time.perf_counter()
    arr.sort() 
    end = time.perf_counter()
    
    ms = (end - start) * 1000
    times[i] = ms
    
    print(f"{key:<15} | {ms:>10.2f} ms")

avg_time = np.mean(times)
print("-" * 35)
print(f"{'TRUNG BÌNH':<15} | {avg_time:>10.2f} ms")
