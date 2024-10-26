# https://projecteuler.net/problem=55

ITERATION_LIMIT = 50


def main():
    counter = 0
    for i in range(1, 10000):
        counter += 1 if is_lynchrel(i) else 0
    print(counter)


def is_lynchrel(num):
    for i in range(1, ITERATION_LIMIT):
        reverse = reverse_number(num)
        candidate = num + reverse
        if is_palindrome(candidate):
            return False
        num = candidate
    return True


def reverse_number(x):
    s = str(x)
    s = s[::-1]
    return int(s)


def is_palindrome(x):
    return x == reverse_number(x)


main()
