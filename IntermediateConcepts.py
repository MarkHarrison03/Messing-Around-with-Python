cost = float(input("How much is each metre squared of tiling?\n"))
width = float(input("Enter width\n"))
height = float(input("Enter height\n"))
num = cost * width * height

print(("{}{}".format(num, " euros")))