import random as rand
import time 

nums=rand.sample(range(1,1000000),10000)
print("before Sorting : " ,nums)

start_time = time.perf_counter()

# Selection sort
# for i in range(len(nums)):
#     min_index=i
#     for j in range(i+1,len(nums)):
#         if nums[min_index]>nums[j]:
#             min_index=j
#     nums[min_index],nums[i]=nums[i],nums[min_index]

#insertion sort
for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

end_time = time.perf_counter()
print("After Sorting : " ,nums)
print("Time taken :",abs(start_time-end_time))