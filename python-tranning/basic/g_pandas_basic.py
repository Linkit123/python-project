import pandas as pd


def main_pandas_basic():
    # indexing()
    return


def example_1():
    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
            "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
            "area": [8.516, 17.10, 3.286, 9.597, 1.221],
            "population": [200.4, 143.5, 1252, 1357, 52.98]}
    brics = pd.DataFrame(dict)
    # Set the index for brics
    brics.index = ["BR", "RU", "IN", "CH", "SA"]
    print(brics)


def indexing():
    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
            "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
            "area": [8.516, 17.10, 3.286, 9.597, 1.221],
            "population": [200.4, 143.5, 1252, 1357, 52.98]}
    brics = pd.DataFrame(dict)
    # Set the index for brics
    brics.index = ["BR", "RU", "IN", "CH", "SA"]
    print(brics['country'])
    print('----------')
    print(brics[['country', 'population']])
