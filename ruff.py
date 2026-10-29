
def Insert_Merge_Interval(nums: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    from bisect import bisect
    insort_pos = bisect(nums, new_interval)

    # how many to the left should i pop, how many to the right should i pop
    left, right = 0, 0
    for i in range(insort_pos - 1, -1, -1):
        start, end = nums[i]
        if end >= new_interval[0]:
            left += 1
            continue
        break
    new_interval[0] = nums[insort_pos - left][0] if left else new_interval[0]


    for i in range(insort_pos, len(nums)):
        start, end = nums[i]
        if start <= new_interval[1]:
            right += 1
            continue
        break

    new_interval[1] = nums[insort_pos + right - 1][1] if right else new_interval[1]

    del nums[insort_pos - left: insort_pos + right]
    # insort(nums, new_interval) # saving one more O(logn) time
    nums.insert(insort_pos - left, new_interval)
    return nums


a = [[1, 3], [4, 5], [6, 7], [8, 10]]
b = [5, 6]
print(Insert_Merge_Interval(a, b))

a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
b = [4, 9]
print(Insert_Merge_Interval(a, b))
