nums = []

while True :
    n = input("Input Number ('no' to stop): ")
    if n.strip('-').isnumeric() :
        n = float(n)
        nums.append(n)
    else :
        length = len(nums)
        nums.sort()

        if length == 0 :
            print("No Median")
        elif length == 1 :
            print("Median: {}".format(nums[0]))
        elif length % 2 == 0 :
            print("Median: {}".format((nums[length//2 - 1] + nums[length//2])/2))
        else :
            print("Median: {}".format(nums[length//2]))
        break
        