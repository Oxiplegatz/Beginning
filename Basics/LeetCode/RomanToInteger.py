class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        exceptions = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return roman_numbers.get(s[-1])
        if s[-2:] in exceptions:
            return self.roman_to_int(s[:-2]) + exceptions.get(s[-2:])
        return self.roman_to_int(s[:-1]) + roman_numbers.get(s[-1])

        # Another Solution:
        #
        # result_number = roman_numbers.get(s[-1])
        #
        # for index in range(len(s) - 2, -1, -1):
        #     if s[index] == 'I' and s[index + 1] in ['V', 'X']:
        #         result_number -= roman_numbers.get(s[index])
        #     elif s[index] == 'X' and s[index + 1] in ['L', 'C']:
        #         result_number -= roman_numbers.get(s[index])
        #     elif s[index] == 'C' and s[index + 1] in ['D', 'M']:
        #         result_number -= roman_numbers.get(s[index])
        #     else:
        #         result_number += roman_numbers.get(s[index])
        #
        # return result_number

check1 = Solution().roman_to_int('XIV')
check2 = Solution().roman_to_int('XXXIV')
check3 = Solution().roman_to_int('CMXLIII')
print(check1)
print(check2)
print(check3)
