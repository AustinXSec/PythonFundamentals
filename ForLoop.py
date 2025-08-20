#for loops = execute a block of code a fixed number of times. 
#For Loops can iterate over a range, string, sequence, etc.

#Looping through a range of numbers
def example1():
    for x in range(1, 11):
        print(x)
    print("HAPPY NEW YEAR")

#Looping through a list
def example2():
    fruits = ["apple","banana","cherry"]
    for x in fruits:
        print(x)


#Looping through a string
def example3():
    for x in "coconut":
        print(x)

#The break statement stops the loop before it has looped through all the items
def example4():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
         break

#The continue statement stops the currents iteraiton of the loop, and continue with the next. 
def example5():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)

#The else keyword in a for loop specifies a block of code to be executed when the loop if finished.
#NOTE: The else block will not be executed if the loop is stopped by a break statement.
def example6():
    for x in range(6):
        print(x)
    else:
        print("Finished")

#A nested loop is a loop inside a loop.
#NOTE:The "inner loop" will be executed one time for each iteration of the "outerloop".
def example7():
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

#A for loop cannot be empty, but if there is reason to have a for loop with no content, put a pass statement to avoid an error. 
def example8():
    for x in [0,1,2]:
        pass
