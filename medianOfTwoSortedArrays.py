class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lsts = nums1 + nums2
        lst_s = sorted(lsts) 
        if len(lst_s) % 2 == 1:
            return lst_s[len(lst_s) // 2]
        else:
            return (lst_s[len(lst_s) // 2 ] + lst_s[(len(lst_s) // 2 - 1 )]) / 2
