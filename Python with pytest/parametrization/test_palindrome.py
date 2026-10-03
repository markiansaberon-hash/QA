import pytest
from is_palindrome import is_palindrome, make_it_backwards

# def test_is_palindrome_empty_string():
#     assert is_palindrome("")

# def test_is_palindrome_single_character():
#     assert is_palindrome("a")

# def test_is_palindrome_mixed_casing():
#     assert is_palindrome("Bob")

# def test_is_palindrome_with_spaces():
#     assert is_palindrome("Never odd or even")

# def test_is_palindrome_with_punctuation():
#     assert is_palindrome("Do geese see God?")

# def test_is_palindrome_not_palindrome():
#     assert not is_palindrome("abc")

# def test_is_palindrome_not_quite():
#     assert not is_palindrome("abab")

@pytest.mark.smoke
@pytest.mark.parametrize("palindrome", ["", "a", "Bob", "Never odd or even", "Do geese see God?"])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.smoke
@pytest.mark.parametrize("not_palindrome", ["abc", "abab"])
def test_is_not_palindrome(not_palindrome):
    assert not is_palindrome(not_palindrome)

# @pytest.mark.parametrize("maybe_palindrome, expected_result",[
#     ("", True),
#     ("a", True),
#     ("Bob", True),
#     ("Never odd or even", True),
#     ("Do geese see God?", True),
#     ("abc", False),
#     ("abab", False)
# ])
# def test_is_palindrome(maybe_palindrome, expected_result):
#     assert is_palindrome(maybe_palindrome) == expected_result

def test_make_it_backwards():
    assert make_it_backwards("hello") == "olleh"