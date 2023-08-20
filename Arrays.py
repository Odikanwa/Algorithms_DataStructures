"""Given an array of integers, find the sum of its elements. 
For example, if ar = [1, 2, 3], 1 + 2 + 3 = 6. So, return 6."""

def array_sum(arr):
    sum = 0
    for num in arr:
        sum = sum + num
    return sum

example = array_sum([1,2,3])
print(example)