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

def longest_nondecreasing_subsequence(lst):
    max_length = 0
    max_sum = float('-inf')
    max_sequence = []

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all(lst[k] <= lst[k+1] for k in range(i, j)):
                current_length = j - i + 1
                current_sum = sum(lst[i:j+1])
                if current_length > max_length or (current_length == max_length and current_sum > max_sum):
                    max_length = current_length
                    max_sum = current_sum
                    max_sequence = lst[i:j+1]
    return max_sequence
    


with open('input.txt', 'r') as file:
    nums = [int(symbol) for symbol in list(file.readline().strip())]

print(len(nums))
print(findLongest(nums))
print(longest_nondecreasing_subsequence(nums))