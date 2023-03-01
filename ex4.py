def rev_str(s: str, _idx: int = 0) -> str:
    tmp = s[_idx]
    reverse_idx = len(s) - _idx - 1

    res = replace_at(s, s[reverse_idx], _idx)
    res = replace_at(res, tmp, reverse_idx)

    if _idx == (len(s) - 1) // 2:
        return res
    else:
        return rev_str(res, _idx + 1)

def replace_at(s: str, replacement: str, idx: int):
    return s[:idx] + replacement + s[idx + 1:]

def main():
    s = "Testando!"
    print(s,"->",rev_str(s))
    print(rev_str(s) == s[::-1])

if __name__ == "__main__":
    main()