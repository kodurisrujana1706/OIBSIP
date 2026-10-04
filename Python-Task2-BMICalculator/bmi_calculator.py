print("================================")
print("       BMI CALCULATOR")
print("================================")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values.")
    else:
        bmi = weight / (height ** 2)

        print("--------------------------------")
        print(f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Category: {category}")
        print("--------------------------------")

except ValueError:
    print("Error: Please enter numbers only.")
