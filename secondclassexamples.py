#name = input("What is your name?")
#print ("Nice to meet you", name)
try:
 #  age = input("How old are you: ")
    print("in 2032 you will be: ", int(age) + 10)
    print(100/int(age))


except ValueError:
   print("Hey, that is not a number")
except ZeroDivisionError:
    print("Can not divide by zero")
except:
    print("This is an error that I did not see")
finally:
    print(" This is what we do after all is done")


