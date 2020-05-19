norm = 0

while True :
    val = input("Enter data point or vector component Value (type no to quit):")
    if val.strip("-").isnumeric() :
        val = float(val)
        norm += val**2
    else :
        break

norm **= 0.5
print("The norm is: {}".format(norm))

   
