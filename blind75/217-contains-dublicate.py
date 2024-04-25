# Given an integer array nums, return true if any value appears at least twice in the arraw, and return false if every element is distinct


def hashset_solution(nums: list) -> bool:
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")
    print("This solution uses a Hashset")
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


def linear_comparison_solution(nums: list) -> bool:
    print("Time Complexity: O(n^2)")
    print("Space Complexity: O(1)")
    print("This solution uses linear search for every iteration")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
