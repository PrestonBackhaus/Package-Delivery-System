import pandas
from package import Package

def create_packages():
    # Dataframe that reads excel file, data starts on row 8 and columns A to G
    df = pandas.read_excel('data/WGUPS Package File.xlsx', header=None, skiprows=8, usecols='A:G')

    # Create packages from dataframe and add to list (for testing), hash table
    packages = []
    for i, row in df.iterrows(): # Each row is a tuple
        id, address, city, state, zip, deadline, weight = row
        package = Package(*row)
        packages.append(package)

# Test to make sure pacakages are created and added correctly
'''for package in packages:
    print(package.get_all_info())'''