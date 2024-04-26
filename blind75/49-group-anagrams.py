from typing import List, DefaultDict


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    m = DefaultDict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        m[tuple(count)].append(s)
    return m.values()
