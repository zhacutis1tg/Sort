import numpy as np

n = 1_000_000
np.random.seed(42)

floats = np.random.uniform(-1_000_000, 1_000_000, (5, n))

floats[0].sort()
floats[1] = np.sort(floats[1])[::-1]

ints = np.random.randint(-1_000_000, 1_000_000, (5, n))

np.savez_compressed(
    'data.npz',
    asc = floats[0], desc = floats[1],
    rand1 = floats[2], rand2 = floats[3], rand3 = floats[4], 
    rand4 = ints[0], rand5 = ints[1], rand6 = ints[2], rand7 = ints[3], rand8 = ints[4]
)