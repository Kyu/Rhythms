import string


def fizz_buzz():
    res = str()
    a = list()

    for i in range(1, 100):
        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"
        if not res:
            res = str(i)
        a.append(res)
        res = str()
    return a


def reverse_string(word):
    return word[::-1]
    # for i in range(len(word), 0, -1):
    # print(word[i])


def pig_latin(sentence):
    pass


def count_vowels(sentence):
    vowels = "aeiou"
    sums = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    total = 0

    for i in sentence:
        if i.lower() in vowels:
            sums[i.lower()] += 1

    for v in sums.values():
        total += v

    return total, sums


def is_palindrome(sentence):
    return sentence == reverse_string(sentence)


def count_words(sentence):
    words = 0
    for i in range(0, len(sentence)):
        if sentence[i] in string.ascii_letters + string.digits:
            if i != 0:
                if sentence[i-1] in string.whitespace:
                    words += 1
            else:
                words += 1

    return words


def text_editor():
    pass
