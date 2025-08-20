#Repeats a piece of code until the condition becomes False.
def example1():
    n = 1
    while n <= 3:
        print(n)
        n +=1

#The break statement stops the loop even if the while condition is True:
def example2():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1

def example3():
    i = 0
    while i < 6:
        i+=1
        if i == 3:
            continue
        print(i)

