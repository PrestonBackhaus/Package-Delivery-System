import csv
from package import Package


def create_packages():
    packages = []

    # Open csv and read data into package objects
    with open('../data/packageCSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create package and add to list of packages
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], "At the hub")
            packages.append(package)

    return packages

