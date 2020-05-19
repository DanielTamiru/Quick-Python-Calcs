var = 0
total = 0
nums = []

while True :
    n = input("Input Number ('no' to stop): ")
    if n.strip('-').isnumeric() :
        n = float(n)
        total += n
        nums.append(n)
    else :
        if len(nums) == 0 :
            print("Empty Data Set")
        else :
            avg = total/len(nums)
            for n in nums :
                var += (n - avg)**2
            print("Variance: {}".format(var))
        break


