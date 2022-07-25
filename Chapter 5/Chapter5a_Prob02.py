import os
os.system('cls||clear')

#----CODE STARTS HERE------
nums = []
i = 0
divisible_num = 0
while i < 10:
    temp = int(input())
    nums.append(temp)
    i += 1

nums.sort()

for index in nums:
    if index % 3 == 0:
        divisible_num += 1


print(f"Highest: {nums[9]}")
print(f"Lowest: {nums[0]}")
print(f"{divisible_num} numbers divisible by 3")
