class Solution(object):
    def twoSum(self, nums, target):
        #num=[2,7,11,15], target=[9]
        #creating a dictionary to store the numbers, {value:index position}
        dictionary = {}
        #index = 0, value = 2
        for index, value in enumerate(nums):
            diff = target - value
            print(diff)
            #diff = 9-2 = 7, 7 wont be in dict yet
            if diff in dictionary:
                print(value)
                print(index)
                #o
                return (index, dictionary[diff])
        #so dictionary[2] = 0, dictionary[7] = 1,
            dictionary[value] = index
            print(dictionary)
        return None
solution = Solution()

# Call the twoSum method
result = solution.twoSum(nums=[3,2,4], target=6)

# Output the result
print(result)

#EXPLANATION FOR AN EXAMPLE WITH INPUT ARRAY = [2,7,11,15] AND TARGET = 9
#WE CREATE EMPTY DICTIONARY
#WE USE ENUMERATE PYTHON BUILT-IN FUNCTION THAT WILL LOOP THROUGH A LIST
# AND GIVE US THE VALUE AND ALSO THE INDEX OF THE NUMBER IN THE LIST
#LOOP 1 DICTIONARY = {}, [3,2,4], TARGET=6 FOR INDEX, VALUE IN ENUM[3,2,4]
#DIFF = 6-3 = 3 -> IF 3 IN DICTIONARY, FIRST LOOP WE HAVE EMPTY DICTIONARY, SO 3 IS NOT THERE
#DICTIONARY[VALUE] = INDEX ==> DICTIONARY[3] = 0 NOW OUR DICTIONARY LOOKS ={3:0, }
#LOOP2, DIFF = 6-2 = 4 -> IF 4 IN DICTIONARY, NO WE HAVE ONLY 3. SO
#DICTIONARY[VALUE] = INDEX ==> DICTIONARY[2] = 1 NOW OUR DICTIONARY LOOKS LIKE ={3:0, 2:1}
####
#LOOP3, DIFF = 6-4 = 2 -> IF 2 IN DICTIONARY, YES WE HAVE 2 IN POSITION 1
#SO WE RETURN THE OUTPUT [INDEX OF CURRENT VALUE FROM LOOP, INDEX OF NUMBER 2 IN DICTIONARY
#RETURN(2, 1)
#PRINT(RESULT) = (2,1)