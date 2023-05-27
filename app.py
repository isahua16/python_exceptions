# try:
#     print(3 + "0")
# except TypeError:
#     print("You must enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except:
#     print("Something went wrong")
# finally:
#     print("Done")

def get_user_number():
    try:
        user_number = input("Please enter a number: ")
        user_number = float(user_number)
        return user_number
    except ValueError:
        print("You must enter a valid number")
    except:
        print("Failure")

first_number = get_user_number()
second_number = get_user_number()

try: 
    print(first_number + second_number)
except TypeError:
    print("You have entered invalid numbers. Try again")
except:
    print("Something went wrong")
finally:
    print("Program finished")


