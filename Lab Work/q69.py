def test(nums, n):
   return(all(x > n for x in nums))      

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("list numbers :",nums)
n = 12
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))
n = 5
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))