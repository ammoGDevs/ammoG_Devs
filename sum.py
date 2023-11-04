def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Get user input
n = int(input("Enter a positive integer: "))

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = calculate_sum(n)
    print(f"The sum of the first {n} numbers is: {result}")
