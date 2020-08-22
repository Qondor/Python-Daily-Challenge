def bmi(weight, height):
    """Body Mass Index calculator.

    Takes weight (in kilograms) and height (in meters) and returns grade of weight.
    """

    result = weight / (height**2)
    if result <= 18.5:
        return "Underweight"
    if result <= 25.0:
        return "Normal"
    if result <= 30.0:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    print(bmi(73, 1.82))