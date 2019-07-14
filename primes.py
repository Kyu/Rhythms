def sieve(n):
    # All numbers are prime until proven otherwise
    array = [i for i in range(1, n+1)]
    primes = array

    for i in array:
        for j in primes:
            if i != j and j % i == 0:
                primes.remove(j)
    return primes
