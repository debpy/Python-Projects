import functools
import time

@functools.lru_cache(2)
def cached_function(value):
    for i in range(value):
        i*i

def timed():
    start_time=time.time()
    cached_function(4647)
    print(f"Duration: {time.time() - start_time}")

timed()
timed()