def main_dictionary():
    # remove()
    return


def example_1():
    phonebook = {"Link": 84342950417, "Xu": 84342950417}
    print(phonebook)


def iterating():
    phonebook = {"Link": 84342950417, "Xu": 84342950417}
    for name, phone_number in phonebook.items():
        print("Phone number of %s is %d" % (name, phone_number))


def remove():
    phonebook = {"Link": 84342950417, "Xu": 84342950417, "Tuesday_1": 111111111, "Tuesday_2": 22222222}
    del phonebook["Tuesday_1"]
    phonebook.pop("Tuesday_2")
    print(phonebook)