"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Input: 3
Output: "III"
"""
def integers_to_roman(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res

def test_sum():
    assert integers_to_roman(81) == "LXXXI", "Should be LXXXI"
    assert integers_to_roman(9) == "IX", "Should be IX"

if __name__ == "__main__":
    test_sum()
