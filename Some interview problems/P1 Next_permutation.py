#https://www.codingninjas.com/studio/problems/893046?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=3

# from itertools import permutations
# def nextPermutation(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     all_perms = [list(i) for i in list(permutations(sorted(nums)))]
#     return all_perms[(all_perms.index(nums)+1)%len(nums)]

# This is not the most optimal solution having time complexity - O(N!*N)
# The next_permutation is an inbuild method in C++ STL functions. 
# Lets try to understand the striver code for this:
def next_permutation(nums):
    n = len(nums)
    # we are traversing the list in reverse till we find an element which is smaller than its successive one.
    # {2,1,5,4,3,0,0} -> n=7, so we start from second last(comparing it to last,hence we started with n-2 not n-1)
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            ind = i
            break
    #now suppose the ind = -1 (its like the case [3,2,1] , we need [1,2,3]), we simply need to reverse the list
    if ind == -1:
        nums.reverse()
        return nums
    
        # we have to find the smallest out of rest of the numbers starting from ind till last such a way that it is next bigger bumber.
        # In [2,1,5,4,3,0,0], the nums[ind] gives value 1, we look from 1 onwards for next small out of [5,4,3,0,0] in reverse order -> 3 
    for i in range(n-1,ind,-1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i] #[2,1,5,4,3,0,0] -> [2,3,5,4,1,0,0]
            break
    #next, we simply need to arrange in ascending order, easiest being simply reverse the descending list from index ind. in-memory.
    nums[ind+1:] = reversed(nums[ind+1:]) #[5,4,1,0,0] -> [0,0,1,4,5]
    return nums ##[2 3 0 0 1 4 5 ]

print(next_permutation([2,1,5,4,3,0,0]))