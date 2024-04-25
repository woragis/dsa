# Given an integer array nums, return all triplets


def bruteforce_solution(nums: list) -> list:
    solution = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    solution.append([i, j, k])
    return solution


def pointer_solution(nums: list) -> list:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        low, r = i + 1, len(nums) - 1
        while low < r:
            three_sum = a + nums[low] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                low += 1
            else:
                res.append([a, nums[low], nums[r]])
                low += 1
                while nums[low] == nums[low - 1] and low < r:
                    low += 1
    return res
