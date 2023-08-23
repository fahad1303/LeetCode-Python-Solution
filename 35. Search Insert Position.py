def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while high >= low:
            mid = (low+ high)//2
            if(nums[mid]>target):
                high= mid-1
            elif(nums[mid]< target):
                low = mid+1
            elif(nums[mid]== target):
                return(mid)

        return low
