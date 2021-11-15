
class Solution:
    def __init__(self):
        pass

    def findMedianSortedArrays(nums1,nums2):
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        
        mid = len(nums1)//2
        x = (nums1[mid] + nums1[~mid]) / 2
        return x

x = Solution
output = x.findMedianSortedArrays([3,4,5],[1,6,8,9])
print(output)