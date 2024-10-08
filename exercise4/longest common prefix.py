class Solution(object):
    def longestCommonPrefix(self, strs):
        #IF NO INPUT PASSED RETURN EMPTY STRING
        if not strs:
            return ""
        #PREFIX = STRS[0] ==> PREFIX = FLOWER
        prefix = strs[0]
        #FOR STRING IN STRS[1:] START FROM WORD [1] IN [0,1,2...], SO FOR STRING IN [FLOW, FLIGHT]
        for string in strs[1:]:
            print(string)
            #while flow.find(flower) not equal =0 flow does not start with flower so shorten the prefix
            #while flow.find(flowe) not equal =0 flow does not start with flower so shorten the prefix
            #while flow.find(flow) not equal =0 flow does not start with flower so shorten the prefix
            #flow = flow so flow will become prefix
            #flight.find(flow) => flight.find(flo) => flight.find(fl) => fl is found in flight so we finalise fl
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
solution = Solution()
output = solution.longestCommonPrefix(["flower","flow","flight"])
print(output)