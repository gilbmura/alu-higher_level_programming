#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):  # Check if input is a string
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(roman_string)):
        # If current numeral is smaller than the next one, subtract its value
        if (
            i + 1 < len(roman_string)
            and roman_map[roman_string[i]] < roman_map[roman_string[i + 1]]
        ):
            total -= roman_map[roman_string[i]]
        else:
            total += roman_map[roman_string[i]]

    return total
