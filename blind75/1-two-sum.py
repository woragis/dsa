def combination_solution(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums) - i):
            if nums[i] + nums[j] == target:
                return [i, j]


def hashmap_solution(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return [i, hashmap[target - nums[i]]]
        hashmap[nums[i]] = i
