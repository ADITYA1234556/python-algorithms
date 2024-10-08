class Solution(object):
    def vowelStrings(self, words, left, right):
        # newlist = [words[i] for i in range(left, right + 1)]
        vowels = 'aeiou'
        number = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                number += 1
        return number
solution = Solution()
output = solution.vowelStrings(words= ["hey","aeo","mu","ooo","artro"], left= 1, right= 4)
print(output)