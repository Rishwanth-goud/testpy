def check_palindrome(input_string):
    
    input_string = input_string.lower()
    reversed_string = input_string[::-1]
    

    if input_string == reversed_string:
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')


check_palindrome("racecar")

