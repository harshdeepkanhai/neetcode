class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]


solution = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
print(solution)

solution = Solution().isPalindrome(s="race a car")
print(solution)

solution = Solution().isPalindrome(s=" ")
print(solution)