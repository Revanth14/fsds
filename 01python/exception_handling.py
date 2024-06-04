a=10
b=0


try:
    print("Resource Opened")
    print(a/b)
    number=int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as e:
    print("You cannot divide by Zero")
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something went wrong")

finally:
    print("Resource Closed")

print("Bye")