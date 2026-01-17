def is_armstrong(number):
    """
    Checks if the given number is an Armstrong number.
    Returns True or False.
    """
    temp = number
    digits = 0

    while temp > 0:
        digits += 1
        temp //= 10

    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == number

print(is_armstrong(153))  # True
print(is_armstrong(9474)) # True
print(is_armstrong(123))  # False
