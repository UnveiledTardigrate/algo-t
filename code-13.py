"""
Roman numerals use seven symbols: I, V, X, L, C, D, and M, 
which represent 1, 5, 10, 50, 100, 500, and 1000.

Numbers are usually written from largest to smallest, left to right. 
But in some cases, a smaller number before a larger one means subtraction:

I before V or X makes 4 or 9
X before L or C makes 40 or 90
C before D or M makes 400 or 900

For example:
II = 2
XII = 12
XXVII = 27
IV = 4
IX = 9

Convert a Roman numeral to an integer.
"""

def romanToInt(s: str) -> int:
    """Converts a Roman numeral string to an integer."""

    # Create a dictionary to map Roman numerals to their integer values
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize the result with the value of the last numeral
    result = roman_numerals[s[-1]]

    # Iterate through the string from left to right (excluding the last numeral)
    for i in range(len(s) - 1):
        # If the current numeral is less than the next one, subtract its value
        # This is because in Roman numerals, a smaller numeral placed before a larger one means subtraction
        if roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
            result -= roman_numerals[s[i]]
        # Otherwise, add its value
        else:
            result += roman_numerals[s[i]]

    return result

# Test cases
assert romanToInt("III") == 3
assert romanToInt("IV") == 4
assert romanToInt("IX") == 9
assert romanToInt("XXVII") == 27
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994