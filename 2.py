import math
def main():
    try:
        value = float(input("Please enter a real value: "))
        sqrt_value = math.sqrt(value)
        print(f"The square root of {value}is {sqrt_value:.2f}")
    except ValueError:
        print("please enter the valid real number")
    except Exception as e:
        print(f"An error occurred :{e}")
    return

