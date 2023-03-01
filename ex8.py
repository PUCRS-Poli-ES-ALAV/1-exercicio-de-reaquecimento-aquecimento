def is_palindrome(s: str, _idx: int = 0) -> bool:
    if _idx > (len(s) - 1) / 2:
        return True
    
    a = s[_idx]
    b = s[len(s) - _idx - 1]

    if a != b: 
        return False
    else:
        return is_palindrome(s, _idx + 1)

def test_is_palindrome(s: str):
    print(f'It is {str(is_palindrome(s)).lower()} that {s} is a palindrome.')

def main():
    test_is_palindrome("aa")
    test_is_palindrome("ab")
    test_is_palindrome("abba")
    test_is_palindrome("aboba")
    test_is_palindrome("adoba")

if __name__ == "__main__":
    main()

