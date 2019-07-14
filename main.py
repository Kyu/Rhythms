from random import randint

from sorting import bubble_sort, merge_sort
from collatz_conjecture import collatz
from primes import sieve

if __name__ == "__main__":
    # bubble_sort(array_length=5000)
    # merge = merge_sort(array_length=5000)
    # print("Merge Sorted Array: \n", merge)

    n = randint(2, 5000)
    print("Collatz(n={n}): {col} iterations".format(n=n, col=collatz(n)))

    n = randint(2, 100000)
    print("Prime numbers from 1 to {n}:\n{primes}".format(n=n, primes=sieve(n)))
