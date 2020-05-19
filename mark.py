grade = 0
mark = 0
total_weight = 0

while True :
    weighting = input("Weighting: (to quit, type 'no'): ")
    if weighting.isnumeric() :
        weighting = float(weighting)
        if input("Mark as a Fraction or Percentage? F for fraction and P for percentage.").lower() == "f":
         num = float(input("Marks earned: "))
         denom = float(input("Out of: "))
         mark = (num / denom) * weighting
        else :
         percentage = float(input("Percent mark: "))
         mark = (percentage / 100) * weighting
    
        total_weight += weighting
        grade += mark
    
    else :
        if (total_weight == 0) :
            print("No Mark")
        else :
             grade = (grade / total_weight) * 100
             print("Your grade is {}%".format(grade))
        break