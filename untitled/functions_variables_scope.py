def print_something():
    s = "this is a string from inside the function"
    print(s)


s = "this is a string from outside the function"
print_something()

print(s)