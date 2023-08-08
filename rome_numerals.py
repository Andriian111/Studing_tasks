"""Roman numeral, any of the symbols used in a system of numerical notation based 
on the ancient Roman system. The symbols are I, V, X, L, C, D, and M, standing respectively 
for 1, 5, 10, 50, 100, 500, and 1,000 in the Hindu-Arabic numeral system. 
A symbol placed after another of equal or greater value adds its value; e.g., 
II = 2 and LX = 60. A symbol placed before one of greater value subtracts its value; e.g., 
IV = 4, XL = 40, and CD = 400. A bar placed over a number multiplies its value by 1,000.
"""


def rome_num(string):
# From 'string' to 'integer'
        rom_val = {
       'M': 1000, 'CM':900,'D': 500, 'CD':400,'C': 100, 'XC':90,  'L': 50, 
       'XL': 40, 'X': 10, 'IX': 9, 'V': 5,'IV':4, 'I': 1}
        i = 0
        result = 0
        while i<len(string):
            if i+1<len(string) and string[i:i+2] in rom_val:
                result += rom_val[string[i:i+2]]
                i+=2
            else:
                result += rom_val[string[i]]
                i+=1
        return result
# print(f"1999 - {rome_num(1999)}")
print(rome_num('CDXLIII'))
print(rome_num("CMXCV"))