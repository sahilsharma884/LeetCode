# Peform 2's compliment for negative number
def twocomplement(arr):
	i = 32
	while i>=0 and arr[i] == 0:
		i -= 1
	i -= 1
	while i>=0:
		if arr[i] == 1:
			arr[i] -= 1
		else:
			arr[i] += 1
		i -= 1
	return arr

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = [0]*33 # Initialize with zero
        for num in nums:
            # If number if positive
            if num>=0:
                s = bin(num).replace("0b","").zfill(33) # Convert into binary and replace special string into empty space and filled it into 33 bits digit
                s = list(map(int,list(s))) # convert string into list
            # If number if negative
            else:
                s = bin(num).replace("-0b","").zfill(33) # Convert into binary and replace special string into empty space and filled it into 33 bits digit
                s = list(map(int,list(s))) # convert string into list
                s[0] = 0 # make starting index as 0
                s = twocomplement(s) # Then get 2's complement of that number

            # Add both 2 list
            result = [sum(x) for x in zip(s,result)]

        result = [x%3 for x in result] # Take a modulus of 3
        result = "".join([str(x) for x in result]) # Convert into string
        if result[0] == '1': # If first bit is 1 means it's a negative number, then
            result = list(map(int,list(result))) # Convert back into list
            result = twocomplement(result) # Take 2's complement of that number to get into positive
            result = "".join([str(x) for x in result]) # make it string from list
            return -1*int(result,2) # Get result with multiply by -1 als0
        else:
            return int(result,2) # just get result
