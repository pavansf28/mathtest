# Math operation functions


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


# Test functions
def main():
    """Run tests for math functions."""
    sum_result = add(2, 5)
    print("The sum of 2 and 5 is:", sum_result)

    difference_result = subtract(10, 4)
    print("The difference between 10 and 4 is:", difference_result)


if __name__ == "__main__":
    main()    
