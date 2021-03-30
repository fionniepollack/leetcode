# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # Check all possible combinaations in list that add up to target
        # Get the indices of the 2 integers that add up to target
        
        # Iterate over list
        # Set first value to check
        # Set second value to check
        # Check if sum of first and second values equal target
        # If sum equals target, return indices for nums
        # Else, keep checking
        
        
        for i, num in enumerate(nums):
            inital_num = num
            index_of_inital_num = i
            nums_to_check = nums[i+1:len(nums)]
            
            for idx, num_to_check in enumerate(nums_to_check):
                sum = inital_num + num_to_check
                if sum == target:
                    index_of_num_to_check = idx
            
                    index_of_correct_num = index_of_num_to_check + index_of_inital_num + 1
            
                    indices = [index_of_inital_num, index_of_correct_num]
        
                    return indices