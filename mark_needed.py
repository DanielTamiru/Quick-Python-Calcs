desired_grade = float(input("Your desired mark out of 100: "))
weight_of_last = float(input("Weight of missing/last grade: "))
mark_so_far = 0 
total_weight = weight_of_last
print("Now let's tally up your marks so far...")

while True :
    weight = input("Weighting: (to quit, type 'no'): ")
    if weight.strip("-").isnumeric() :
        weight = float(weight)
        percentage = float(input("Percent mark: "))
        mark_so_far += (percentage / 100) * weight
        total_weight += weight

    else :
        needed = 100 * ((desired_grade/100 * total_weight - mark_so_far) / weight_of_last)
        print("You need at least a(n) {}%".format(needed))
        break