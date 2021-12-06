import re


def main_module_and_package():
    # example_1()
    return


def example_1():
    find_members = []
    for member in dir(re):
        if "find" in member:
            find_members.append(member)

    print(sorted(find_members))