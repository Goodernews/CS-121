
def duplicate(string, number):
    # Repeats string as many times as possible in the space specified
    available_spaces = number - len(string)
    num_repeats = available_spaces // len(string) + 1
    return string * num_repeats
"""
    if len(string)>number:
        return ""
    else:
        num_repeats = number//len(string)
        return num_repeats*string
"""