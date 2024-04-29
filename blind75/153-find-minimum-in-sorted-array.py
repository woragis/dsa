from typing import List


def optimal_binary_search_solution(nums: List) -> int:
    res = nums[0]
    left, r = 0, len(nums) - 1
    while left <= r:
        if nums[left] < nums[r]:
            res = min(res, nums[left])
            break
        mid = (left + r) // 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            r = mid - 1
    return res
