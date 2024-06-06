class Solution(object):
    @classmethod
    def romanToInt(cls, s):
        """
        :type s: str
        :rtype: int
        """
        rom_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # numbers = [1, 2, 3, 4, 5]
        #
        # def square(number):
        #     return number ** 2
        # squared = map(square, numbers)
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        s = sum(map(lambda x: rom_to_int[x], s))
        print(s)
        # s = s.replace('IV', '4')
        # s = s.replace('IX', '9')
        # s = s.replace('IL', '40')
        # s = s.replace('XC', '90')
        # s = s.replace('CD', '400')
        # s = s.replace('CM', '900')
        # print(s)
        # # print(rom_to_int.keys())
        # for i in s:
        #     if i.isdigit():
        #         continue
        #     s = s.replace(i, str(rom_to_int[i]))
        #     #     continue
        #     # mapp.append(rom_to_int[i])
        # print(s)
        # s = s.replace('0', '')
        # print(s)


if __name__ == "__main__":
    Solution.romanToInt(s='MCMXCIV')
