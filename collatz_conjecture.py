def collatz(num):
    runs = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 1 + num * 3
        runs += 1

    return runs
