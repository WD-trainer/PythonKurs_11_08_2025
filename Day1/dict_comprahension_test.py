import timeit

# Number of items in the dictionary
N = 10000

# Test dictionary comprehension
def dict_comprehension():
    return {i: i ** 2 for i in range(N)}

# Test regular dictionary creation
def dict_regular_loop():
    d = {}
    for i in range(N):
        d[i] = i ** 2
    return d

# Measure execution time using timeit
comprehension_time = timeit.timeit("dict_comprehension()", globals=globals(), number=100)
loop_time = timeit.timeit("dict_regular_loop()", globals=globals(), number=100)

print(f"Dictionary comprehension time: {comprehension_time:.4f} seconds")
print(f"Regular loop time: {loop_time:.4f} seconds")
print("Comprehension is faster!" if comprehension_time < loop_time else "Loop is faster!")