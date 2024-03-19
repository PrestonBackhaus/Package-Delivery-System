import csv


def create_addresses():
    addresses = []

    # Open csv and add address only into list
    with open('../data/addressCSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            addresses.append(row[2])

    return addresses


def create_distances():
    distances = []

    # Open csv and add distances into list
    with open('../data/distanceCSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            clean_row = []
            # Change empty strings or 0.0 (distance to itself) to None
            for val in row:
                if val == '':
                    clean_row.append(None)
                else:
                    clean_row.append(float(val))  # Change strings to floats
            distances.append(clean_row)

    return distances

