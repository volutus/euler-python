# https://projecteuler.net/problem=38

all_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
keep_counting = True


def main():
    max_number = 0
    counter = 1
    while keep_counting:
        num = create_pandigital(counter)
        print(f"counter={counter}, num={num}")
        if is_pandigital(num):
            if num > max_number:
                max_number = num
        counter += 1
    print(max_number)


def create_pandigital(num):
    global keep_counting
    if len(str(num)) >= 5:
        keep_counting = False
        return 0

    i = 1
    pan = ""
    while True:
        x = num * i
        pan += str(x)
        if len(pan) >= 9:
            break
        i += 1
    return int(pan)


def is_pandigital(num):
    if len(str(num)) != 9:
        return False

    digits = set()
    for digit in str(num):
        digits.add(digit)
    return digits == all_digits


main()
