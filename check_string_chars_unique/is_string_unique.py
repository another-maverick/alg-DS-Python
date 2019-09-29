
def is_unique(input_string):
    result_chars = {}
    for each_char in input_string:
        char_val = ord(each_char)
        if char_val in result_chars:
            print("The String does not have unique charecters")
            return False
        else:
            result_chars[char_val] = True
    print("Yesss! The string has unique charecters")
    return True

if __name__ == '__main__':
    is_unique("Hey")