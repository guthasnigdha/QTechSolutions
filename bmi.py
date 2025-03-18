def calculate_bmi(weight, height):
   
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

# Taking user input
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
    else:
        bmi, category = calculate_bmi(weight, height)
        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
