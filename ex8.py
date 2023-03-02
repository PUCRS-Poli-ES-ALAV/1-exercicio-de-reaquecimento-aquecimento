def is_palindrome(s: str) -> bool: 
    if len(s) < 2:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

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
