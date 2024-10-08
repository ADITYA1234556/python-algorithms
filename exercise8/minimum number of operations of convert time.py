class Solution(object):
    def convertTime(self, current, correct):
        #"02:30" "04:35"
        #"01234","01 2(:) 34"
        current_time = int(current[:2]) * 60 + int(current[3:])
        correct_time = int(correct[:2]) * 60 + int(correct[3:])
        difference = correct_time - current_time
        iterations = 0
        times = [60, 15, 5, 1 ]
        for i in times:
            if (difference ==0):
                break
            iterations += difference // i
            difference %= i
        return iterations

TIME = input("Enter the current time in format 00:00")
TARGET = input("Enter the target time in format 00:00")
solution = Solution()
output = solution.convertTime(TIME, TARGET)
print(output)

#BREAKDOWN
#CURRENT_TIME = 02:30 (01234) AND TARGET_TIME = 04:35
# INT(CURRENT[:2]) BEFORE THE 2ND ELEMENT (0,1) ==> CURRENT_TIME[0,1] => INT(02) = 2 * 60 = 120
#INT(CURRENT[3:]) AFTER THE THIRD ELEMENT (3,4)==> CURRENT_TIME[3,4] => INT(30) = 30 = 150
#TARGET = 275 => DIFF = 125
#LOOP 1 IF 125 == 0 NO => 0 += 125 // 60 ==> 0 += 2 ==> ITERATIONS = 2 ==> DIFFERENCE %= I => 125 / 60 ==> DIFFERENCE = 5
#LOOP 2 IF 5 == 0 NO => 2 += 5 / 15 CANNOT
#LOOP 3 IF 5 == 0 NO ==> 2 += 5 / 5 => 2 + 1 ==> ITERATIONS = 3 ==> DIFFERENCE %= I => 5 / 5 =0
#LOOP 4 IF 0 == 0 YES BREAK