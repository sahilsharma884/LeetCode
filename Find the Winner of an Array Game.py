class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0] # take first as winner
        j = 1 # Start from second index
        count = 0 # take counter to iterate till 'k' times
        while count < k:
            # If winner already in first index and also prev winner was same, just increment the count
            if arr[0] > arr[j] and arr[0] == winner:
                count += 1
            else: # Otherwise swap the first and jth index
                arr[0],arr[j] = arr[j],arr[0]
                winner = arr[0] # assign new winner
                count = 1 # start counting from 1
            j += 1 # increment the j index
            if count == len(arr): # If count is already compared with all the elements if k=10000000, terminate here and return it
                return winner # no need to go further when it already compared to all the elements
            if j == len(arr): # if j index already reach out at the end, come back to start with j=1
                j = 1
                
        return winner # return winner
                
