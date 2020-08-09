
import sys
import functools

@functools.lru_cache(None)
def cycle(n):
    iterations = 1
    while(n != 1):
        if(n % 2 == 0):
            n = n//2
        else:
            n = (3*n) + 1
        iterations = iterations+1
    return iterations


@functools.lru_cache(None)
def max_cycle(start, end):
    if(start > end):
        start, end = end, start
    return max(cycle(n) for n in range(start, end+1))


for line in sys.stdin:
    start, end = map(int, line.split()[:2])
    print(start, end, max_cycle(start, end))

exit(0)
