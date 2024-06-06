class Solution(object):
    @classmethod
    def longestCommonPrefix(cls, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # print(strs[3][3])
        # print(strs[0][3])


        strs = sorted(map(lambda x: x, strs), key=len, reverse=False)
        pref = ''

        for i in range(len(strs)):
            current = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    print(pref)
            pref += current

    def longestCommonPrefix222(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix

# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(list(second_largest))

if __name__ == "__main__":
    Solution.longestCommonPrefix(["flower", "flow", "flight"])
