x = None

if x:
    print("None is True")
elif x is False:
    print("None is False")
else:
    print("None is not True, or False, None is just None")

x = None
if x is None:
    print("yes")
if x == None:
    print("it does")


def greet():
    print("hello!")


x = greet()
print(x)
