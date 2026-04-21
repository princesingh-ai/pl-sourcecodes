try:
    a =  10
    b = 0
    c = a / b

except ZeroDivisionError:
    print("You cannot divide by zero!")

else:
    print(f"The result is:{c}")

finally:
    print("This block will always execute.")