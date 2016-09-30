print("hi!")
#var_name = input("type something...")

#if var_name == "computing":
#    print("yay!")

# this is a comment
"""
hello
hello
hello
"""

x = 5
y = 6

add = x + y
sub = x - y
mult = x * y
div = x / y

sqr = x ** 2
pwrs = x ** y
mod = x % y


#BIDMAS

answer1 = 4 + 7 * 6 / 3
answer2 = (4 + 7) * 6 / 3

#strings

string1 = "string1"
string2 = "string2"
string3 = "string3"

           #string1 string2 string3
sentence = '{} {} {}'.format(string1, string2, string3)
sentence1 = '{2} {1} {0}'.format(string1, string2, string3)
sentence2 = '{2} {1} {2}'.format(string1, string2, string3)


#line break
print("line1\nthis line will be below") #replace ? with a line break

# -------- Data Types --------

# Type: Int(eger)
one = 1
two = 2

# Type: Float (decimal)
one_point_five = 1.5
three_point_two = 3.2

# Type: String
text1 = 'blah'
text2 = "blah"

# Type: Long
three_billion = 300000000 #It's mega long!

#Type: Boolean (bool or true/false)
yes = True
no = False
result = one == 1 #result = True
result2 = one_point_five >= 3 #result2 = False

# Type casting
three = int("3") #convert string to int
text_four = str(4) #convert int to string
five = int(float("5.7")) #convert string to int
                  # => 5
six_point_zero = float(6) #convert int to float
                # => 6.0

# Array of sunshine...
# ... a list of values

x = [3, 5, 9, 6]

print(x[2]) # show the 3rd value of the 'x' array

x[1] = 4 # edit the 2nd value of the 'x' array

# If..If..If..If..

y = int(input("pick a number"))

if y == 1:
    print("you chose 1!")
elif y==2:
    print("you chose 2!")
elif y==3:
    print("you chose 3!")
else:
    print("Invalid number (needs to be between 1 and 3)")

# Loopty.. loop.. Loop

for x in range(1, 4):
    print(x)

for z in range(0, 12, 3): # 3 times table
    print(z)


# while you wait...
a = 1
while a != 0:
    a = int(input("I'm thinking of a number...?"))
print("Well done, you guessed it!")

# I'm breaking out

for x in range(1000000):
    print(x)
    if x == 20:
        break #let's leave this loop

# Functions

def name_of_function():
    #Stuff the function does...

# This is not indented and as a result not part of
# the 'name_of_function' functon

def sayHello():
    for x in range(6):
        print ("Hello, my name is Jamie. What's yours?")

sayHello()

# 1000 lines later...

sayHello()

# function attributes

def sayHelloToYou(your_name):
    print("Hello " + your_name)

sayHelloToYou("Bob")
sayHelloToYou("Doris")


def sayHelloXTimes(x):
    for i in range(x):
        print("hello")


def anotherFunc(x, y, z):
    #do something

def sometimesDoSomething(x = 0): #'x' is an optional attribute
    if x == 0:
        #do something
    else
        #do something else

def sumNumbers(num1, num2):
    result = num1 + num2
    return result

def subtractNumbers(num1, num2):
    return num1 - num2

answer = sumNumbers(1, 3)
answer2 = subtractNumbers(3, 1)

# Iteration vs Recursion

n = 3
answer = 1
for i = 1 in range(n+1)
	answer = answer * i

#








def factorial(n):
    if n == 0:
		return 1
	else
		return n * factorial(n - 1)










# Mutual recursion
def even(n):
    return True if n == 0 else odd(n - 1)

def odd(n):
    return False if n == 0 else even(n - 1)

even(10)
#True
odd(10)
#False
