import numpy as np


def main_numpy_arr():
    # exercise()
    return


def example_1():
    # Create 2 new lists height and weight
    height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
    weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

    # Create 2 numpy arrays from height and weight
    np_height = np.array(height)
    np_weight = np.array(weight)

    print(np_height)
    print(type(np_height))
    print(np_weight)
    print(type(np_weight))


def calculator():
    # Create 2 new lists height and weight
    height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
    weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

    # Create 2 numpy arrays from height and weight
    np_height = np.array(height)
    np_weight = np.array(weight)

    # Calculate bmi
    bmi = np_weight / np_height ** 2

    # Print the result
    print(bmi)


def sub_setting():
    # Create 2 new lists height and weight
    height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
    weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

    # Create 2 numpy arrays from height and weight
    np_height = np.array(height)
    np_weight = np.array(weight)

    # Calculate bmi
    bmi = np_weight / np_height ** 2

    # For a boolean response
    var1 = bmi > 25
    print(var1)
    # Print only those observations above 23
    var2 = bmi[bmi > 25]
    print(var2)


def exercise():
    weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
    np_weight_kg = np.array(weight_kg)

    np_weight_pound = np_weight_kg*2.2

    print(np_weight_pound)
