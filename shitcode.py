((input_str := input("Enter your friend you wanna check: ")) or True) and (check_palindrome := lambda x: all(c1 == c2 for c1, c2 in zip(x.lower(), reversed(x.lower())))) and (decision_string := lambda is_palindrome, string: f"\"{string}\" is your best friend" if is_palindrome and string else f"\"{string}\" is an imposter" if string else "Do you ever have friends?") and print(decision_string(check_palindrome(input_str), input_str))  # Selected task 3 from given list, except empty string denotes the absence of friends, and it ignores uppercase/lowercase for sake of ability to write names properly. Code runs in CLI for Python 3.8+ versions, just type `python3 shitcode.py` (or just python, idk how it might work on Windows) and enter palindrome you wanna check. That's all.