# https://projecteuler.net/problem=461

"""
I actually took several tries at this before getting a workable solution.
My first attempt used a naive implementation where I first generated the potential values and then used a
4-layer for loop to get the values of A, B, C, and D.
This worked but was too slow.
I then tried to swap this permutation approach for combinations using itertools which was faster, but still too slow.
Then, I tried a greedy approach where I generated the closest possible value first and then tried to plug in
smaller values, but these ended up being less close than the optimal solution.
I ended up finding a bisection approach on the following page which I adapted to create this solution.
This uses a conventional meet-in-the-middle approach which cuts the runtime down significantly.
https://www.ivl-projecteuler.com/overview-of-problems/30-difficulty/problem-461
"""
import math


def main():
    print(approximate_pi(200))        # 10000 ==> 159820276


def approximate_pi(n):
    values = generate_values(n)
    pairs = generate_pairs(values)

    best_difference = math.pi
    best_variables = ()
    for i in range(len(pairs)):
        first_half = pairs[i]
        j = bisect(pairs, math.pi - first_half[0]) - 1
        second_half = pairs[j]
        difference = math.pi - (first_half[0] + second_half[0])
        if difference < 0:
            break
        if difference < best_difference:
            best_difference = difference
            best_variables = (first_half[1], first_half[2], second_half[1], second_half[2])
    answer = square_variables(best_variables)
    return sorted(best_variables), answer


def generate_values(n):
    values = list()

    counter = 0
    while True:
        value = euler_function(n, counter)
        if value > math.pi:
            return values
        values.append(value)
        counter += 1


def generate_pairs(values):
    max_value = len(values)
    pairs = list()
    for i in range(max_value):
        for j in range(i + 1, max_value):
            a = values[i]
            b = values[j]
            approx = a + b
            if approx > math.pi:
                break       # No need to keep going once we're past pi
            pairs.append((approx, i, j))

    pairs = sorted(pairs)
    return pairs


def euler_function(n, k):
    return (math.e ** (k / n)) - 1


def bisect(ls, target):
    # Modified from bisect_right in bisect module to work with tuples easily.
    # Otherwise, we'd need to adapt them all which would be troublesome and would inflate the profile of this program.
    lo = 0
    hi = len(ls)
    while lo < hi:
        mid = (lo + hi)//2
        if target < ls[mid][0]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def square_variables(variables):
    sum = 0
    for variable in variables:
        sum += math.pow(variable, 2)
    return sum


main()
