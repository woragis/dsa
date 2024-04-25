from typing import Dict

# Given two strings s and t, return true if t is an anagram of s, and false otherwise


def sort_solution(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def map_solution(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map1: Dict[str, int] = {}
    map2: Dict[str, int] = {}
    for i in range(len(s)):
        map1[s[i]] = 1 + map1.get(s[i], 0)
        map1[t[i]] = 1 + map2.get(t[i], 0)

    for c in map1:
        if map1[c] != map2.get(c, 0):
            return False
    return True
