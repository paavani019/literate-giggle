def sort(nums):

  
  for i in range(5):
    minpos=i
    for j in range(i, 6):
      if nums[j] < nums[minpos]:
        minpos = j

    temp= nums[i]
    nums[i]= nums[minpos]
    nums[minpos] = temp


nums=[2, 5, 7, 5, 9, 0, 3, 6]

sort(nums)

print(nums)
