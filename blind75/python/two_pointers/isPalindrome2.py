class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        
        while left <= right:

            while left < right and not self.isAlphaNum(s[left]):
                left += 1

            while left < right and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

    def isAlphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

solution = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
print(solution)

solution = Solution().isPalindrome(s="race a car")
print(solution)

solution = Solution().isPalindrome(s=" ")
print(solution)