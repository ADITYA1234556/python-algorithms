class Solution(object):
    def isAlienSorted(self, words, order):
        alien_order = {char: i for i, char in enumerate(order)}
        print(alien_order)
        #order = "hlabcdefgijkmnopqrstuvwxyz" => alien_order = { h: 0, l: 1, a: 2, b: 3, etc}
        # Step 2: Function to compare two words based on alien order
        #word 1 = hello word 2 = leetcode
        def compare_words(word1, word2):
            # Compare characters one by one using zip function
            for char1, char2 in zip(word1, word2):
                if alien_order[char1] < alien_order[char2]:
                    return True  # word1 is smaller, correct order
                elif alien_order[char1] > alien_order[char2]:
                    return False  # word1 is greater, incorrect order
            # If we reach here, the words are identical so far, check lengths

            return len(word1) <= len(word2)

        # Step 3: Check if all words are in sorted order
        for i in range(len(words) - 1):
            if not compare_words(words[i], words[i + 1]):
                return False  # Words are not sorted

        return True

solution = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
output = solution.isAlienSorted(words, order)
print(output)

# zip function combines two lists/tuples and pairts them up based on their position.
# if list1 = [1,2,3,4] list2 = ['a','b','c'] result = zip(list1, list2) print(list(result)) => [(1,'a'), (2,'b'), (3,'c')]
#loop1 if h < l => 0 < 1 True
#loop2 if e < e => identical words so we check their position