nums = {}
mode = []
max_freq = 0
length = 0

while True :
    n = input("Input Number ('no' to stop): ")
    if n.strip('-').isnumeric() :
        length += 1
        n = float(n)
        if n not in nums :
            nums[n] = 1
        else :
            nums[n] += 1
    elif bool(nums) == False:
        print("No Mode")
        break
    else :
        for n in nums :
                if nums[n] > max_freq :
                    mode = [n]
                    max_freq = nums[n]
                elif nums[n] == max_freq :
                    mode.append(n)
        
        if length == len(nums) and length > 1:
            print("No Mode")
        else :
            print("Mode(s): {}".format(mode))
        break