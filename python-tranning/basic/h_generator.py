import random


def main_generator():
    exercise()
    return


def example_1():
    def lottery():
        for i in range(6):
            yield random.randint(2, 23)
        yield random.randint(1, 15)

    for random_number in lottery():
        print("And the next number is... %d!" % random_number)


def exercise():
    # fill in this function
    def fib():
        pass  # this is a null statement which does nothing when executed, useful as a placeholder.


    # testing code
    import types
    if type(fib()) == types.GeneratorType:
        print("Good, The fib function is a generator.")

        counter = 0
        for n in fib():
            print(n)
            counter += 1
            if counter == 10:
                break
