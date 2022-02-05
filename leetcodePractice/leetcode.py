# ✍️ 1. Two Sum  (EASY PART)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# for function으로 활용하기
# class Solution:
#     def twoSum(self, nums, target):

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 sum = nums[i] + nums [j]

#                 if sum == target:
#                      return [i,j]


# class Solution:
#     def twoSum(self, nums, target):

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return [ i, j]






# ✍️ 2. Palindrome Number (EASY PART)

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.



# class Solution:
#     def isPalindrome(self, x):
#         if x > 0:
#             temp = x
#             rev_int_elements = []
#             while temp > 0:
#                 digit = temp % 10
#                 rev_int_elements.append(digit)
#                 temp = temp // 10
#             org_int_elements = rev_int_elements[::-1]
#             return rev_int_elements == org_int_elements
#         elif x == 0:
#             return True
#         else:
#             return False


# math = 6//6
# print(math)

# print(11//3) #floor division