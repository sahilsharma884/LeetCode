class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ###################
        # With Two passes #
        ###################
#         c0,c1,c2 = 0,0,0 # Store the number of 0's,1's,2's
#         for num in nums:
#             if num == 0:
#                 c0 += 1
#             if num == 1:
#                 c1 += 1
#             if num == 2:
#                 c2 += 1
                
#         # Just rearranged it as per number of c0,c1,c2
#         k = -1
#         while c0:
#             k += 1
#             nums[k] = 0
#             c0 -= 1
#         while c1:
#             k += 1
#             nums[k] = 1
#             c1 -= 1
#         while c2:
#             k += 1
#             nums[k] = 2
#             c2 -= 1
            
        ###################
        # With One passes #
        ###################
        c,L = 0,0 # take 2 pointers, cuurent and low value
        H = len(nums)-1 # take H pointers high value
        while c <= H and L<=H: # Iterate till its satisfy
            if nums[c] == 0: # If nums is 0, swap arr[L] and arr[c]
                nums[c],nums[L] = nums[L],nums[c]
                c += 1 # increment current and low index
                L += 1
            elif nums[c] == 1: # if nums is 1, increment current index
                c += 1 
            elif nums[c] == 2: # if nums is 2, swap arr[c] and arr[H]
                nums[c],nums[H] = nums[H],nums[c]
                H -= 1 # decrement high index value
                
                
