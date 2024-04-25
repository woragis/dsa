def solution(s: str) -> bool:
    st = []
    m = {"}": "{", "]": "[", ")": "("}
    for c in s:
        if c in m.keys():
            if st and st[-1] == m[c]:
                st.pop()
            else:
                return False
        else:
            st.append(c)
    return True if not st else False
