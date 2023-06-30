print("Hi! I'm your BMI calculator.\n")

height = input("Enter your height. (EX:1.80) ")
weight = input("Enter your weight. ('KG') ")

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)
new_bmi = str(bmi_as_int)
print("Your BMI is: " + new_bmi)
