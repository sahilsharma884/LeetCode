class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {} # store the seen part character
        max_len = 0 # store to evaluate the length of substring
        start = 0 # start index
        for end in range(len(s)): # iterate from start to end range
            if s[end] in seen: # if charater end index contain in seen part, then
                start = max(start,seen[s[end]] + 1) # change the start index by comparing current start index and index of particular character's end index present
                # in seen part dict.
            
            seen[s[end]] = end # store the key as character at end index with value as end index. {CharAtEndIndx: EndIdx}
            max_len = max(max_len, end - start + 1) # calculate max length of substring. Comparing current max_len and diff. of start and end index.
            # Whichever is greater will be the updated max_len
        
        return max_len
