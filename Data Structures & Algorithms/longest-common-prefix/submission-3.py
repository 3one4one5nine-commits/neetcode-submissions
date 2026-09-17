class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=strs[0]
        for str in strs[1:]:
            for i in range(len(longest)):
                if (i>=len(str) or str[i]!=longest[i]):
                    longest=longest[:i]
                    break
        return longest