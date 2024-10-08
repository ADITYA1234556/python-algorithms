class Solution(object):
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

arr = [1024,512,256,128,64,32,16,8,4,2,1]
# arr = [0, 1, 2, 3, 15, 5, 11, 7, 8]
solution = Solution()
output = solution.sortByBits(arr)
print(output)


""" lambda function can take any number of arguments but can only have one expression ==> add = lambda a,b: a + b ==> print(add(2,3)) ==> 5
bin function convertes integer into binary expression and returs it as a string prefixed with '0b' bin(add) = bin(5) ==> 0b101 
sorted will sort the arr[] by counting the number of 1's in each position and sort them accordingly
"""



#0001 = 1
#0010 = 2
#0011 = 3
#0100 = 4