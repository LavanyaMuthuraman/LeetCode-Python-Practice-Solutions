"""
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.
You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Intuition:
Approach:
1. The function takes a list nums and a target integer target as input.
2. It uses two nested loops to iterate through the elements of the nums list.
3. The outer loop selects an element at index i.
4. The inner loop starts from the next element (index i+1) and checks if the sum of the elements at indices i and j is equal to the target.
5. If a pair of elements is found whose sum equals the target, it returns the indices [i, j].
6. If no such pair is found after checking all combinations, it returns None.
In essence, this approach explores all possible pairs of elements in the nums list to find a pair whose sum matches the target. However, as mentioned earlier, it has a time complexity of O(n^2), which may not be efficient for large input lists.

Complexity:
Time complexity: O(n^2)
Space complexity: O(1) 
'''

#Solution:
class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
object=Solution()
print(object.twoSum([2,7,11,15],9))
