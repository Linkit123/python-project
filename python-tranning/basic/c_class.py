def main_class():
    # exercise()
    return


class MyClass:
    name = "link"
    age = 25

    def print_name(self):
        print(self.name)


class NumberHolder:
    def __init__(self, number):
        self.number = number


def exercise():
    class Vehicle:
        name = ""
        kind = "car"
        color = ""
        value = 100.00

        def __init__(self, name, color, value):
            self.name = name
            self.color = color
            self.value = value

        def description(self):
            desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
            return desc_str

    car1 = Vehicle("Fer", "red", 60000.00)
    car2 = Vehicle("Jump", "blue", 10000.00)

    print(car1.description())
    print(car2.description())
