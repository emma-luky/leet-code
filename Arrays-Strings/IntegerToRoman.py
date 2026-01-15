# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#         ]
#         symb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#         ]
        
#         roman = ""
#         i = 0
#         while num > 0:
#             count = num // val[i]
#             roman += symb[i] * count
#             num %= val[i]
#             i += 1
#         return roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"],
                     [400, "CD"], [100, "C"], [90, "XC"],
                     [50, "L"], [40, "XL"], [10, "X"],
                     [9, "IX"], [5, "V"], [4, "IV"],
                     [1, "I"]]
        for i in range(len(storeIntRoman)):
            count = num // storeIntRoman[i][0]
            roman += storeIntRoman[i][1] * count
            num-= storeIntRoman[i][0] * count
        return roman
