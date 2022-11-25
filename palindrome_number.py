class solution:
    def isPalindrome(self, x: int):
        if x <= 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10: return False
            x = (x % div) // 10
            div = div / 100
        return True

x = solution()
print("Test 1:", x.isPalindrome(1223))
print("Test 2:", x.isPalindrome(0))
print("Test 3:", x.isPalindrome(1221))
print("Test 4:", x.isPalindrome(-1221))
