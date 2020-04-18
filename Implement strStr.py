class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle) is 0):
            return 0
        else:
            return haystack.find(needle)
        