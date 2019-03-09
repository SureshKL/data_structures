"""
Minimum distance between two occurrences of maximum

You are given an array of n-elements with a basic condition that occurrence of
greatest element is more than once. You have to find the minimum distance
between maximums. (n>=2).

Examples:

Input : arr[] = {3, 5, 2, 3, 5, 3, 5}
Output : Minimum Distance = 2
Explanation : Greatest element is 5 and its index
are 1, 4 and 6. Resulting minimum distance of 2
from position 4 to 6.

Input : arr[] = {1, 1, 1, 1, 1, 1}
Output : Minimum Distance = 1
Explanation : Greatest element is 1 and its index
are 0, 1, 2, 3, 4 and 5. Resulting minimum distance
of 1.

Source: https://www.geeksforgeeks.org/minimum-distance-between-two-occurrences-of-maximum/
"""


def find_min_dist(numbers, max_num):
    min_dist = len(numbers)
    temp_index = None

    for i, n in enumerate(numbers):
        if n == max_num:
            if temp_index is not None:
                dist = i - temp_index
                if dist < min_dist:
                    min_dist = dist
            temp_index = i
    return min_dist


if __name__ == '__main__':
    test_cases = {
        (3, 5, 2, 3, 5, 3, 5): {'result': 2},
        (1, 1, 1, 1, 1, 1): {'result': 1},
        (6, 3, 1, 3, 6, 4, 6): {'result': 2},
    }

    st = """
for test_case, inputs in test_cases.items():
    max_num = max(test_case)
    result = find_min_dist(test_case, max_num)
    assert result == inputs['result'], f'Failed - Expected {inputs["result"]}, Got {result}'    
    """

    import timeit

    t = timeit.Timer(stmt=st, globals=globals())
    print(t.repeat(repeat=3))
