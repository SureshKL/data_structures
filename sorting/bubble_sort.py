numbers = [3, 2, 1, 5, 4, 0]

print('#Comparisons Sorted Array')
outer_loop_count = 0
inner_loop_count = 0
for i in range(len(numbers)-1):
    outer_loop_count += 1

    c = 0
    for j in range(len(numbers) - 1 - i):  # -i to skip already sorted elements
        c += 1
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f'{c}'.ljust(12), numbers)
    inner_loop_count += c

print(f'Array length = {len(numbers)}')
print(f'Outer loop ran for {outer_loop_count} times')
print(f'Inner loop ran for {inner_loop_count} times')
"""
Output:

#Comparisons Sorted Array
5            [2, 1, 3, 4, 0, 5]
4            [1, 2, 3, 0, 4, 5]
3            [1, 2, 0, 3, 4, 5]
2            [1, 0, 2, 3, 4, 5]
1            [0, 1, 2, 3, 4, 5]
Array length = 6
Outer loop ran for 5 times
Inner loop ran for 15 times
"""

"""
Time complexity:

# Finding worst case time complexity
(n-1) * (3n-1)
3n^2 - n - 3n + 1   # Equation
3n^2 - 4n + 1       # Initial
3n^2 - 4n           # Removed constant 1
3n^2                # Removed 4n
n^2                 # Removed constant 3

Best case   : O(n) 
Average case: O(n^2) 
Worst case  : O(n^2) 
"""