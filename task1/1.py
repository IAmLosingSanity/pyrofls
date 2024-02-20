def findLongest(nums):
    longest = []
    curr = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] >= nums[i-1]:
            curr.append(nums[i])
        else:
            if len(curr) > len(longest):
                longest = curr
            elif len(curr) == len(longest) and sum(curr) > sum(longest):
                longest = curr
            curr = [nums[i]]

    if len(curr) > len(longest):
        longest = curr
    elif len(curr) == len(longest) and sum(curr) > sum(longest):
        longest = curr

    return longest

with open('input.txt', 'r') as file:
    nums = [int(symbol) for symbol in list(file.readline().strip())]

print(len(nums))
print(findLongest(nums))