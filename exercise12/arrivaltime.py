class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        expected_time = arrivalTime +  delayedTime
        if expected_time > 23:
            output = 24 - expected_time
            return output
        else:
            output = expected_time
            return output

solution = Solution()
arrivalTime = int(input("Enter the expected arrival time in 24 hour format: "))
delayedTime = int(input("Enter the delayed time by hours: "))
output = solution.findDelayedArrivalTime(arrivalTime, delayedTime)
print(f"The expected new arrival time is {output}")