class Solution:
    def twoSum(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = {} # key as element and value as index of an array
        r[arr[0]] = 0 # initially set key and value as first element with index 0
        for i in range(1,len(arr)): # Iterate from index 1 to N elements
            if (target - arr[i]) in r: # Required elements: Target - CurrentElement; Is in present in r dict
                return [i,r[target - arr[i]]] # If yes, just return the [CurrentIndex, IndexFromdict]
            else:
                r[arr[i]] = i # Otherwise add into r dict [CurrentElement: CurrentIndex]
