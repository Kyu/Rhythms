from sorting import *
from collatz_conjecture import *
from primes import *
from text import *
from helpers import *


if __name__ == "__main__":
    # bubble_sort(array_length=5000)
    # merge = merge_sort(array_length=5000)
    # print("Merge Sorted Array: \n", merge)

    n = randint(2, 5000)
    print("Collatz(n={n}): {col} iterations".format(n=n, col=collatz(n)))

    # n = randint(2, 100000)
    # print("Prime numbers from 1 to {n}:\n{primes}".format(n=n, primes=sieve(n)))

    print("Fizz Buzz: 0 -> 100\n{}".format(fizz_buzz()))

    text = rand_string(10)
    print("{text} reversed: {rev}".format(text=text, rev=reverse_string(text)))

    text = rand_string(50)
    print("Vowel composition of {text}: \n{res[0]}: {res[1]}".format(text=text, res=count_vowels(text)))

    # Palindrome test

    text = "This is a sentence\tHey\nNew line? why not. 5 fishes"
    print("Number of words in: (\n{text}\n): {words} words".format(text=text, words=count_words(text)))
