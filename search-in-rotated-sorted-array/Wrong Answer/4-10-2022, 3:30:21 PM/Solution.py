// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearchK(arr, l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if mid != 0 and arr[mid-1] > arr[mid]:
                    return mid
                else:
                    #print(mid, r)
                    if arr[mid] > arr[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            return -1        
        def binarySearch(arr, l, r, x):
            while l <= r:
                mid = l + (r - l) // 2
                print(mid)
                if arr[mid] == x:
                    return mid
                if x > arr[mid]:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        k = binarySearchK(nums, 0, len(nums)-1)
        if k == -1:
            return binarySearch(nums, 0, len(nums)-1, target)
        else:
            if target > nums[0]:
                return binarySearch(nums, 0, k, target)
            else:
                return binarySearch(nums, k+1, len(nums)-1, target)