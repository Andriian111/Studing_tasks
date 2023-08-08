"""
A palindrome is a series of letters or numbers that reads equivocally backwards. Write a recursive function that determines whether a given string is a palindrome or not.

Examples
is_palindrome("Go hang a salami, I'm a lasagna hog!") ➞ True

is_palindrome("This phrase, surely, is not a palindrome!") ➞ False

is_palindrome("Eva, can I see bees in a cave?") ➞ True
"""

def is_palindrome(p):
    string = p.lower()
    char_remove = [',', "'", '!', ' ', '#', '%', ".", "*", '?', '-' ]
    for char in char_remove:
        string = string.replace(char, "")
    if len(string)<=1:
        return True
    else:
        return string[::-1] == string




str_vector, res_vector = [
  "Maneuquenam", "Not a palindrome", "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!",
  "Go hang a salami, I'm a lasagna hog!", "This phrase is really this!", "Red rum, sir, is murder.",
  "Big step on no pets, Gib!", "One True fortune, but no!", "Don't nod.", "I did, did I?", "My gym.",
  "Top spot.", "Was it a cat I saw?", "No lemon, no melon.", "Eva, can I see bees in a cave?",
  "Can I be iconic?", "Madam I'm Adam.", "The man on the moon are them.", "Sit on a potato pan, Otis.",
  "Truly, a classic caddilac!", "Able was I, ere I saw Elba.", "Step on no pets!"
], [
  True, False, True, True, False, True, True, False, True, True, True,
  True, True, True, True, False, True, False, True, False, True, True
]
count = 1
for i in range(0, len(str_vector)):
    print(f"Example {count} = {is_palindrome(str_vector[i])}, result = {res_vector[i]}")
    count +=1

# from re import findall, MULTILINE
# from inspect import getsource

# def check_recursive(fn):
#   try:
#     src, n = getsource(fn), fn.__name__
#     if n == '<lambda>': n = src.split('=')[0].strip()
#     return len(findall(n, src, flags=MULTILINE)) > 1
#   except OSError: return True

# Test.assert_not_equals(check_recursive(is_palindrome), False, 'Recursion is required!')

# str_vector, res_vector = [
#   "Maneuquenam", "Not a palindrome", "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!",
#   "Go hang a salami, I'm a lasagna hog!", "This phrase is really this!", "Red rum, sir, is murder.",
#   "Big step on no pets, Gib!", "One True fortune, but no!", "Don't nod.", "I did, did I?", "My gym.",
#   "Top spot.", "Was it a cat I saw?", "No lemon, no melon.", "Eva, can I see bees in a cave?",
#   "Can I be iconic?", "Madam I'm Adam.", "The man on the moon are them.", "Sit on a potato pan, Otis.",
#   "Truly, a classic caddilac!", "Able was I, ere I saw Elba.", "Step on no pets!"
# ], [
#   True, False, True, True, False, True, True, False, True, True, True,
#   True, True, True, True, False, True, False, True, False, True, True
# ]
# for i, n in enumerate(str_vector): Test.assert_equals(is_palindrome(n), res_vector[i])