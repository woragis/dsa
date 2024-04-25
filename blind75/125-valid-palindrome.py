def solution(s: str) -> bool:
    sf = ""
    for c in s:
        if c.isalnum():
            sf += c
    sf = sf.lower()
    return sf == sf[::-1]
