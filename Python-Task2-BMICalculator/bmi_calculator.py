def calculate_bmi():
    print("================================")
    print("       BMI CALCULATOR")
    print("================================")

    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters: "))

            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be positive values.")
                continue

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            print("\n--------------------------------")
            print(f"Your BMI: {bmi:.2f}")
            print(f"Category: {category}")
            print("--------------------------------")

            break

        except ValueError:
            print("Error: Please enter valid numeric values.")


calculate_bmi()
