
def twoSum(nums, target: int):
    for index, value in enumerate (nums):
        # nums.pop(index)
        print("index is:", index)
        print("value is:", value)
        
        for i in range(index+1, len(nums)):
            print("inner index is:", i)
            print("inner value is:", nums[i])
            sum_x = value+nums[i]
            print("sum is:", sum_x)
            print("target is:", target)
            if (sum_x == target):
                
                return [index, i] 


a = [2,7,11,15]
t = 9
output = twoSum(a,t)
print (output)