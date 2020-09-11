class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2): # From argument, we assume, number of elements is nums1 is less than nums2. Otherwise swap it
            return self.findMedianSortedArrays(nums2,nums1)
    
        # Store length of nums1 and nums2
        x = len(nums1)
        y = len(nums2)
        
        low = 0 # low index value
        high = x # high index value
        
        while low <= high: # iterate while low less than and equal to high index value
            partitionX = (low + high)//2 # Take median index value using low and high
            partitionY = (x + y + 1)//2 - partitionX # Take median value using lengths of nums1 and nums2
            
            # Store max_left_x, min_right_x, max_left_y, min_right_y
            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf') # if number exist in nums1, then store value otherwise assign minus infinity
            minRightX = nums1[partitionX] if partitionX < x else float('inf') # same as above
            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf') # same as above
            minRightY = nums2[partitionY] if partitionY < y else float('inf') # same as above
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX: # Max of left x should be less than and equal to min of Right y. And vice versa of x and y.
                if (x + y) % 2 == 0: # If numbers of both elements is even, then
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2 # take average of max(lefts of x and y) and min(rights of x and y)
                else: # otherwise
                    return max(maxLeftX, maxLeftY) # take max(lefts of x and y)
            elif maxLeftX > minRightY: # if max of left x greater than min of right y, then
                high = partitionX - 1 # shift the high index value to left
            else: # otherwise
                low = partitionX + 1 # shift the low index value to right
