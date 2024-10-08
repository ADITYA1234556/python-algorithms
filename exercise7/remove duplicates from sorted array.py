class Solution(object):
    def removeDuplicates(self, nums):
        empty_list = []
        for i in nums:
            if i not in empty_list:
                empty_list.append(i)
            else:
                empty_list.append("_")
        return empty_list
solution = Solution()
numbers = input("Print a list of numbers (comma seperated) ").split(",")
print(numbers)
A = [int(i) for i in numbers]
print(A)
output = solution.removeDuplicates(A)
print(output)