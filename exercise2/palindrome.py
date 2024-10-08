class Solution(object):
    def isPalindrome(self, x):
        word = x.lower()
        word_reversed = word[::-1]

        if word_reversed == word:
            return("It is a palindrome")
        else:
            return("It is not a palindrome")

a = input("Please type the word that you want to see if it is a palindrome: ")
solution = Solution()
output = solution.isPalindrome(a)
print(output)


# b = input("Please type the word that you want to check if is a palindome: ").lower()
# reversed_b = b[::-1]
# if reversed_b == b:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")
# print(reversed_b)

#to see if the given integer or string is a palindrome,
# palindrome is something that returns the same value even when reversed
#like RADAR, 121, LEVEL, 111, ETC.

