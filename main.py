user_input = input("Enter a real number: ")
try:
    number=float(user_input)
    if number >= 0:
        square_root = number ** 0.5
        print(f"Square root of {number} is {square_root:.2f}")
    else:
        print('Square root is underfine for negative number ')
except ValueError:
    print("Invalid input.please enter a valid real number")