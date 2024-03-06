import pandas

# Dataframe reads excel file, from 9 to 35, columns C to AC
df = pandas.read_excel('data/WGUPS Distance Table.xlsx', header=None)

# addressData list, contains all hub addresses
addressData = df.iloc[8:35, 1].values.tolist()

# distanceData list, contains all distances from hub to hub
distanceData = df.iloc[8:35, 2:29].values.tolist()

# Test
for address in addressData:
    print(address)
for distance in distanceData:
    print(distance)
print(distanceData[2][0])