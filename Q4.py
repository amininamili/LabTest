#4(a)
def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
    function = x
    print("Arguments are ", function, "and will return", multiply_by_two(function))

print_arguments(x)
    
augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)


#4(b)
def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    function = x
    print("2 * (", x, " * 3)")

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)


#4(c)
def add_numbers(a, b):
    return a + b

def augmented_function(function, decorators):
    function = a
    decorators = b
    print("(2 * (", function, "+ ", decorators, "))")

decorated_function = augmented_function(add_numbers,[print_arguments, multiply output])

x = decorated_function(3,4)