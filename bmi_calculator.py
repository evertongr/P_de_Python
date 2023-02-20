height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/height**2, 2)

# if(bmi < 17):
#     print("Your bmi is: " + str(bmi) + ". Muito abaixo do peso.")
# elif(bmi >=17 and bmi <18.5):
#     print("Your bmi is: " + str(bmi) + ". Abaixo do peso.")
# elif(bmi >=18.5 and bmi <25):
#     print("Your bmi is: " + str(bmi) + ". Peso normal.")
# elif(bmi >=25 and bmi <30):
#     print("Your bmi is: " + str(bmi) + ". Acima do peso.")
# elif(bmi >=30 and bmi<35):
#     print("Your bmi is: " + str(bmi) + ". Obesidade I.")
# elif(bmi >=35 and bmi<40):
#     print("Your bmi is: " + str(bmi) + ". Obesidade II.")
# else:
#     print("Your bmi is: " + str(bmi) + ". Obesidade III.")

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
