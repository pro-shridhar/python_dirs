nums_squared_lc = [num**2 for num in range(5)]  # example of iltrator
nums_squared_gc = (num**2 for num in range(5))  # example of generator


for item in nums_squared_gc:
    # The for loop itself iterates over
    # the original list

    try:
        print(f"Next item from iterator: {item}")
        next_item = next(nums_squared_gc)
    except StopIteration:
        print("Iterator exhausted.")
        break
