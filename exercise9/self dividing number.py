class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        #if self dividing will append to result
        for i in range(left, right + 1):
            num = i
            #num = 9
            while i:
                x = num % 10
                #x = 9 / 10 = 9
                if x == 0: #if 9 == 0 false
                    break
                if i % x != 0: #if 9 % 9 not equal to zero break it is zero so false and will continue
                    break
                num //=10 #9 /10 = 0.9 roud off = 0 so result.append(9)

            if num == 0:
                result.append(i)
        return result


LEFT = int(input("Enter the start range: "))
RIGHT = int(input("Enter the finish range: "))
solution = Solution()
output = solution.selfDividingNumbers(LEFT, RIGHT)
print(output)



# input left = 1 right = 22, have to find self dividing number from 1 to 22.
# range = [1, 22 +1] => range [1, 23]
#self dividing numbers => 12 because 12 / 1 == 0 12 / 2 == 0 remainder
#num 13
#x = 13 % 10 = 3 => 3 != 0 if 13 % 3 = 1 not equal to zero it is true 13 /10 = 1.3 not zero so miss
#x = 12 % 10 = 2 => 2 != 0 if 12 % 2 = 0 is equal to zero it is false so add it to result