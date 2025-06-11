print ("hello world")
def generate_subsets(nums, index=0, current_subset=None):
    if current_subset is None:
        current_subset = []
        
    if index == len(nums):
        print(current_subset)
        return
    
    generate_subsets(nums, index + 1, current_subset + [nums[index]])
    generate_subsets(nums, index + 1, current_subset)

numbers = [1, 2, 3]
generate_subsets(numbers)
