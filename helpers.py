import time
import string
import random


def timeit(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\nfunc:{fname} args:[{args}, {kwargs}] took {length:.3f} secs"
              .format(fname=func.__name__, length=end-start, args=args, kwargs=kwargs))
        return result
    return timed


def rand_string(length):
    s = ''.join(
        random.SystemRandom().choice(string.ascii_letters + string.digits + "     ") for _ in range(length))
    return s
