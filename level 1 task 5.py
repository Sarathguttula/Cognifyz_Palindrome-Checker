def is_palindrome(s):
    """
    Checks if the given string is a palindrome.
    Ignores case and spaces.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    text = input("Enter a word or phrase to check for palindrome: ")
    if is_palindrome(text):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")