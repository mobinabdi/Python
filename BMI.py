w = 75

h = 180

bmi = w / ((h / 100) ** 2)

print(bmi)
if bmi < 18.5:
    print("Kambod vazen")
elif  18.5 < bmi < 24.9:
    print("Ideal")
elif bmi > 25:
    print("azaf vazne")
