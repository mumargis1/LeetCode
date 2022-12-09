class Solution:
    def longestPalindrome(self, s: str):
        def check_plain(s):
            return (s==s[::-1])


        biggest = s[0]
        step = biggest//2

    # for single letter center
        for center in range(1, len(s)-1):
            bounds = [center-(1+step), center+(1+step)]
            while (bounds[0]>-1) and (bounds[1]<len(s)):
                if check_plain(s[bounds[0]:bounds[1]+1]):
                    biggest = s[bounds[0]:bounds[1]+1]
                    step = biggest//2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break

        for center in range()