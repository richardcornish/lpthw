# Exercise 21
# http://learnpythonthehardway.org/book/ex21.html

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


# Study drill #1
# Let's break it down, step by step
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = add(add(30, 5), subtract(subtract(78, 4), multiply(multiply(90, 2), divide(divide(100, 2), 2))))
# what = add(35, subtract(74, multiply(180, divide(50, 2))))
# what = add(35, subtract(74, multiply(180, 25)))
# what = add(35, subtract(74, 4500))
# what = add(35, -4426)
# what = -4391

# Study drill #2
number = 3
what_2 = add(age, subtract(height, multiply(weight, divide(iq, number))))
print "When we change the number to %d, we get" % number, what_2

# Study drill #3
what_3 = 5 + (10 - (3 * (4 / 2)))
what_3 = 5 + (10 - (3 * divide(4, 2)))
what_3 = 5 + (10 - multiply(3, divide(4, 2)))
what_3 = 5 + subtract(10, multiply(3, divide(4, 2)))
what_3 = add(5, subtract(10, multiply(3, divide(4, 2))))
print "When I make my own crazy-ass equation, it's %d" % what_3
