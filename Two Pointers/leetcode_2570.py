from typing import List
'''
    Merge Two 2D Arrays by Summing Values
'''
class Solution:
    def twoPointers(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        i = j = 0
        result= []
        while i<n and j<m:
            if nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i=i+1
            elif nums1[i][0] > nums2[j][0]:
                result.append(nums2[j])
                j=j+1
            else:
                nums1[i][1]=nums1[i][1]+nums2[j][1]
                result.append(nums1[i])
                i=i+1
                j=j+1

        result.extend(nums1[i:n])
        result.extend(nums2[j:m])
        return result


nums1 = [[1,2],[2,3],[3,4],[5,6]]
nums2 = [[1,2],[3,4],[4,2],[5,6]]
solution = Solution()
res = solution.twoPointers(nums1, nums2)
print(res)
