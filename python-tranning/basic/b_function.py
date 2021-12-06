def main_function():
    # call function here
    # exercise()
    return


def my_function():
    print("Hello function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , I wish you %s" % (username, greeting))


def sum_number(a, b):
    return a + b


def exercise():
    def list_benefits():
        return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and "
                                                                                  "connect code together"]

    def build_sentence(name):
        return "%s is a benefit of functions!" % name

    def concat_name():
        benefits = list_benefits()
        for benefit in benefits:
            print(build_sentence(benefit))

    concat_name()
