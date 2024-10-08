class Solution(object):
    def romanToInt(self, s):
        string = s.upper()
        result_number = 0
        prevous_number = 0
        mapping = {
                   'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000
        }
        #for e.g input is XIV = VIX,
        # V => MAP[V] >= PREVIOUS NUMBER => 5 >=0 => RESULTNUM += MAP[V] => 0+5 => RESULT_NUM = 5 AND PREV_NUM = MAP[SYMBOL] => PREV_NUM = 5
        # I => MAP[I] >= PREVIOUS NUMBER => 1 >= 5 =>  RESULTNUM -= MAP[V] => 5-1 => RESULT_NUM = 4 AND PREV_NUM = 1
        # X => MAP[X] >= PREVIOUS NUMBER => 10 >=1 => RESULTNUM += MAP[V] => 4+10 = 14
        for symbol in string[::-1]:

            if mapping[symbol] >= prevous_number:
                result_number += mapping[symbol]
            else:
                result_number -= mapping[symbol]
            prevous_number = mapping[symbol]
        return result_number

solution = Solution()
a =  input("Please type a roman letter: ")
output = solution.romanToInt(a)

print(output)