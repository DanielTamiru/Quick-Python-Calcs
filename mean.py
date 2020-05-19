total = 0
num = 0

while True :
    n = input("Input Number ('no' to stop): ")
    if n.strip('-').isnumeric() :
        n = float(n)
        total += n
        num += 1
    else :
        if num == 0 :
            print("No Average")
        else :
            print("Average: {}".format(total/num))
        break

