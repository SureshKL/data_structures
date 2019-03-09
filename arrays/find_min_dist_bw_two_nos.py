"""
Find the minimum distance between two numbers

Given an unsorted array arr[] and two numbers x and y, find the minimum
distance between x and y in arr[]. The array might also contain duplicates.
You may assume that both x and y are different and present in arr[].

Examples:
Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 and 2 is 1.

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 and 5 is 2.

Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
Output: Minimum distance between 3 and 6 is 4.

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, x = 3, y = 2
Output: Minimum distance between 3 and 2 is 1.

Source: https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/
"""


def find_min_distance(numbers, x, y):
    min_dist = len(numbers)
    x_pos = y_pos = None
    for i, n in enumerate(numbers):
        if n == x:
            x_pos = i
            if y_pos is not None:
                dist = abs(y_pos - x_pos)
                if dist < min_dist:
                    min_dist = dist
            continue

        if n == y:
            y_pos = i
            if x_pos is not None:
                dist = abs(y_pos - x_pos)
                if dist < min_dist:
                    min_dist = dist
    return min_dist


if __name__ == '__main__':
    test_cases = {
        (1, 2): {'x': 1, 'y': 2, 'result': 1},
        (3, 4, 5): {'x': 3, 'y': 5, 'result': 2},
        (3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3): {'x': 3, 'y': 6, 'result': 4},
        (2, 5, 3, 5, 4, 4, 2, 3): {'x': 3, 'y': 2, 'result': 1},
    }

    st = """
for test_case, inputs in test_cases.items():
    x, y = inputs['x'], inputs['y']
    result = find_min_distance(test_case, x, y)
    assert result == inputs['result'], f'Failed - Expected {inputs["result"]}, Got {result}'
    # print(f'Min distance between {x} & {y} is {result}')
    """

    import timeit

    t = timeit.Timer(stmt=st, globals=globals())
    print(t.repeat(repeat=3))
