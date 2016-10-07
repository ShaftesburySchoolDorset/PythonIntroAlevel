# Global vs local variables

gv = 6 # This is our global variable
gv += 3 # We can change the value of gv at the same level without issue

def one():
    # we can read global variables without any other declartions
    # BUT it's not recommended!
    print('gv value is: ', gv)

def oneCorrected():
    global gv # You need this is you're going to use a global variable
    print('gv value is: ', gv)

def two():
    lv = 11 # a variable local to the function; a.k.a local variable
    print('the memory address of lv (func two) is: ', hex(id(lv)))

def three():
    lv = 12 # another local variable, local to a different function
    print('the memory address of lv (func three) is: ', hex(id(lv)))

def four():
    global gv
    gv = 8
    print('the memory address of gv (func four) is: ', hex(id(gv)))

def five():
    global gv
    gv = 9
    print('the memory address of gv (func five) is: ', hex(id(gv)))

one()
oneCorrected()
two()
three()
four()
five()

print("""\nAs you can see, the memory address of the gv variable is the same in
both functions four and five, this means they are accessing the same block
of memory. Whereas in functions two and three the addresses are different,
so although the (local) variables have the same name, they are stored in and
accessed from different memory locations.""")
