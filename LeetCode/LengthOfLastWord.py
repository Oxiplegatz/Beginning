class Solution:
    def length_of_last_word(self, s: str) -> int:
        # words = s.split()
        # last_word = words[-1].strip()
        #
        # return len(last_word)

        s = s.strip()
        if ' ' not in s:
            return len(s)
        else:
            word = ''
            for index in range(len(s) - 1, -1, -1):
                if s[index] == ' ' or s[index] is None:
                    return len(word)
                word += s[index]


check1 = Solution().length_of_last_word("   fly me   to   the moon  ")
check2 = Solution().length_of_last_word("a")
check3 = Solution().length_of_last_word("  11  23 a hello mate      %%%@#$ wher e  is the ll ast word 00   ")

print(check1)
print(check2)
print(check3)
