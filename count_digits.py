def count_digits (number):
    counter = 0
    x = abs(number)  # Take the absolute value to handle negative numbers
    while True:
        x = x//10
        counter += 1
        if x == 0:
            return counter

try:
    n = int(input("Enter a number: "))

    # Call the count_digits function and display the result
    print(f"There are {count_digits(n)} digits in {n}.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
