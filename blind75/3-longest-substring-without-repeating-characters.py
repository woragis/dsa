# Given a string s, find the length of the longest substring without repeating characters.

from typing import Set


def solution(s: str) -> int:
    charSet: Set[str] = set()
    left = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[r])
        res = max(res, r - left + 1)
    return res
