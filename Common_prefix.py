class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # we will use horizontal scanning, where we will compare characters column-wise across all strings.
        
        # we will loop over each character index i of the first string
        for i in range(len(strs[0])):
            #for each index i we will check every string s in list strs
            for s in strs:
                # if the current string length is sorter than i, or if there is mismatch in character at the same index then we can't continue comparing
                if i == len(s) or s[i]  != strs[0][i]:
                    # we will return everything up to index i
                    return s[:i]
        # if no mismatch found and all the character match till the end of the first string then we the entire first string will be common prefix
        return strs[0]