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


# ✍️ 2. Add Two Numbers Leetcode Problem 2


# class Solution:


#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         final_list = t3 = ListNode()
#         carry = 0
#         while l1 != None or l2 != None or carry:
#             v1, v2 = 0, 0
#             if l1:
#                 v1 = l1.val
#                 l1 = l1.next
#             if l2:
#                 v2 = l2.val
#                 l2 = l2.next
#             sum1 = v1 + v2 + carry
#             if sum1 > 9:
#                 carry = 1
#             else:
#                 carry = 0
#             value = sum1 % 10
#             t3.next = ListNode(value)
#             t3 = t3.next

#         return final_list.next


# Longest Substring Without Repeating Characters - Leetcode 3 - Python
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#                 charSet.add(s[r])
#                 res = max(res, r-l +1)
#         return res
