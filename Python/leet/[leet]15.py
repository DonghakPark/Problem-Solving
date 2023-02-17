"""
3Sum Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""
from itertools import combinations
# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     if len(nums) < 3:
#         return []
#     else:
#         answer = []
#         combi = list(combinations(nums, 3))
#         for element in combi:
#             if sum(element) == 0:
#                 temp = sorted(list(element))
#                 if temp not in answer:
#                     answer.append(temp)
#
#         return answer

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_temp = nums[i] + nums[left] + nums[right]
                if sum_temp < 0:
                    left += 1
                elif sum_temp > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer


if __name__=="__main__":
    solution = Solution()

    nums1 = [-1,0,1,2,-1,-4]
    nums2 = []
    nums3 = [0]

    print(solution.threeSum(nums1))
    print(solution.threeSum(nums2))
    print(solution.threeSum(nums3))

