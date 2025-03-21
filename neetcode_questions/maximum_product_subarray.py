def maxProduct(nums):
    if not nums:
        return 0  # Edge case: Empty array

    max_product = min_product = result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # Since num could be negative, we swap max and min when num < 0
        print(max_product, min_product)
        if num < 0:
            max_product, min_product = min_product, max_product
        
        print(max_product, min_product)
        print("\n")

        # Compute the max and min product ending at the current index
        max_product = max(num, num * max_product)
        min_product = min(num, num * min_product)

        # Update result with the best maximum found so far
        result = max(result, max_product)

    return result

# Example Usage
print(maxProduct([0, -2, 0, -3, 4, -1, -2, -3, -4]))