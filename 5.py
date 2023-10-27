height = float(input("please enter your height:"))
weight = int(input("please enter your weight:"))
bmi = weight / height**2
if bmi < 18.5:
    print(f"your bmi is {bmi},you are underweight")
elif bmi > 25:
    print(f"your bmi is {bmi}, you are overweight")
else:
    print(f"your bmi is {bmi}, you are normal weight")