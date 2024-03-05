#Data to be added:
'''"Package
ID"	Address	City 	State	Zip	"Delivery
Deadline"	"Weight
KILO"
1	195 W Oakland Ave	Salt Lake City	UT	84115	10:30 AM	21
2	2530 S 500 E	Salt Lake City	UT	84106	EOD	44
3	233 Canyon Rd	Salt Lake City	UT	84103	EOD	2
4	380 W 2880 S	Salt Lake City	UT	84115	EOD	4
5	410 S State St	Salt Lake City	UT	84111	EOD	5
6	3060 Lester St	West Valley City	UT	84119	10:30 AM	88
7	1330 2100 S	Salt Lake City	UT	84106	EOD	8
8	300 State St	Salt Lake City	UT	84103	EOD	9
9	300 State St	Salt Lake City	UT	84103	EOD	2
10	600 E 900 South	Salt Lake City	UT	84105	EOD	1
11	2600 Taylorsville Blvd	Salt Lake City	UT	84118	EOD	1
12	3575 W Valley Central Station bus Loop	West Valley City	UT	84119	EOD	1
13	2010 W 500 S	Salt Lake City	UT	84104	10:30 AM	2
14	4300 S 1300 E	Millcreek	UT	84117	10:30 AM	88
15	4580 S 2300 E	Holladay	UT	84117	9:00 AM	4
16	4580 S 2300 E	Holladay	UT	84117	10:30 AM	88
17	3148 S 1100 W	Salt Lake City	UT	84119	EOD	2
18	1488 4800 S	Salt Lake City	UT	84123	EOD	6
19	177 W Price Ave	Salt Lake City	UT	84115	EOD	37
20	3595 Main St	Salt Lake City	UT	84115	10:30 AM	37
21	3595 Main St	Salt Lake City	UT	84115	EOD	3
22	6351 South 900 East	Murray	UT	84121	EOD	2
23	5100 South 2700 West	Salt Lake City	UT	84118	EOD	5
24	5025 State St	Murray	UT	84107	EOD	7
25	5383 South 900 East #104	Salt Lake City	UT	84117	10:30 AM	7
26	5383 South 900 East #104	Salt Lake City	UT	84117	EOD	25
27	1060 Dalton Ave S	Salt Lake City	UT	84104	EOD	5
28	2835 Main St	Salt Lake City	UT	84115	EOD	7
29	1330 2100 S	Salt Lake City	UT	84106	10:30 AM	2
30	300 State St	Salt Lake City	UT	84103	10:30 AM	1
31	3365 S 900 W	Salt Lake City	UT	84119	10:30 AM	1
32	3365 S 900 W	Salt Lake City	UT	84119	EOD	1
33	2530 S 500 E	Salt Lake City	UT	84106	EOD	1
34	4580 S 2300 E	Holladay	UT	84117	10:30 AM	2
35	1060 Dalton Ave S	Salt Lake City	UT	84104	EOD	88
36	2300 Parkway Blvd	West Valley City	UT	84119	EOD	88
37	410 S State St	Salt Lake City	UT	84111	10:30 AM	2
38	410 S State St	Salt Lake City	UT	84111	EOD	9
39	2010 W 500 S	Salt Lake City	UT	84104	EOD	9
40	380 W 2880 S	Salt Lake City	UT	84115	10:30 AM	45
'''

packages = {
    "1": {"Address": "195 W Oakland Ave", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "10:30 AM", "Weight": "21"},
    "2": {"Address": "2530 S 500 E", "City": "Salt Lake City", "State": "UT", "Zip": "84106", "Deadline": "EOD", "Weight": "44"},
    "3": {"Address": "233 Canyon Rd", "City": "Salt Lake City", "State": "UT", "Zip": "84103", "Deadline": "EOD", "Weight": "2"},
    "4": {"Address": "380 W 2880 S", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "EOD", "Weight": "4"},
    "5": {"Address": "410 S State St", "City": "Salt Lake City", "State": "UT", "Zip": "84111", "Deadline": "EOD", "Weight": "5"},
    "6": {"Address": "3060 Lester St", "City": "West Valley City", "State": "UT", "Zip": "84119", "Deadline": "10:30 AM", "Weight": "88"},
    "7": {"Address": "1330 2100 S", "City": "Salt Lake City", "State": "UT", "Zip": "84106", "Deadline": "EOD", "Weight": "8"},
    "8": {"Address": "300 State St", "City": "Salt Lake City", "State": "UT", "Zip": "84103", "Deadline": "EOD", "Weight": "9"},
    "9": {"Address": "300 State St", "City": "Salt Lake City", "State": "UT", "Zip": "84103", "Deadline": "EOD", "Weight": "2"},
    "10": {"Address": "600 E 900 South", "City": "Salt Lake City", "State": "UT", "Zip": "84105", "Deadline": "EOD", "Weight": "1"},
    "11": {"Address": "2600 Taylorsville Blvd", "City": "Salt Lake City", "State": "UT", "Zip": "84118", "Deadline": "EOD", "Weight": "1"},
    "12": {"Address": "3575 W Valley Central Station bus Loop", "City": "West Valley City", "State": "UT", "Zip": "84119", "Deadline": "EOD", "Weight": "1"},
    "13": {"Address": "2010 W 500 S", "City": "Salt Lake City", "State": "UT", "Zip": "84104", "Deadline": "10:30 AM", "Weight": "2"},
    "14": {"Address": "4300 S 1300 E", "City": "Millcreek", "State": "UT", "Zip": "84117", "Deadline": "10:30 AM", "Weight": "88"},
    "15": {"Address": "4580 S 2300 E", "City": "Holladay", "State": "UT", "Zip": "84117", "Deadline": "9:00 AM", "Weight": "4"},
    "16": {"Address": "4580 S 2300 E", "City": "Holladay", "State": "UT", "Zip": "84117", "Deadline": "10:30 AM", "Weight": "88"},
    "17": {"Address": "3148 S 1100 W", "City": "Salt Lake City", "State": "UT", "Zip": "84119", "Deadline": "EOD", "Weight": "2"},
    "18": {"Address": "1488 4800 S", "City": "Salt Lake City", "State": "UT", "Zip": "84123", "Deadline": "EOD", "Weight": "6"},
    "19": {"Address": "177 W Price Ave", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "EOD", "Weight": "37"},
    "20": {"Address": "3595 Main St", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "10:30 AM", "Weight": "37"},
    "21": {"Address": "3595 Main St", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "EOD", "Weight": "3"},
    "22": {"Address": "6351 South 900 East", "City": "Murray", "State": "UT", "Zip": "84121", "Deadline": "EOD", "Weight": "2"},
    "23": {"Address": "5100 South 2700 West", "City": "Salt Lake City", "State": "UT", "Zip": "84118", "Deadline": "EOD", "Weight": "5"},
    "24": {"Address": "5025 State St", "City": "Murray", "State": "UT", "Zip": "84107", "Deadline": "EOD", "Weight": "7"},
    "25": {"Address": "5383 South 900 East #104", "City": "Salt Lake City", "State": "UT", "Zip": "84117", "Deadline": "10:30 AM", "Weight": "7"},
    "26": {"Address": "5383 South 900 East #104", "City": "Salt Lake City", "State": "UT", "Zip": "84117", "Deadline": "EOD", "Weight": "25"},
    "27": {"Address": "1060 Dalton Ave S", "City": "Salt Lake City", "State": "UT", "Zip": "84104", "Deadline": "EOD", "Weight": "5"},
    "28": {"Address": "2835 Main St", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "EOD", "Weight": "7"},
    "29": {"Address": "1330 2100 S", "City": "Salt Lake City", "State": "UT", "Zip": "84106", "Deadline": "10:30 AM", "Weight": "2"},
    "30": {"Address": "300 State St", "City": "Salt Lake City", "State": "UT", "Zip": "84103", "Deadline": "10:30 AM", "Weight": "1"},
    "31": {"Address": "3365 S 900 W", "City": "Salt Lake City", "State": "UT", "Zip": "84119", "Deadline": "10:30 AM", "Weight": "1"},
    "32": {"Address": "3365 S 900 W", "City": "Salt Lake City", "State": "UT", "Zip": "84119", "Deadline": "EOD", "Weight": "1"},
    "33": {"Address": "2530 S 500 E", "City": "Salt Lake City", "State": "UT", "Zip": "84106", "Deadline": "EOD", "Weight": "1"},
    "34": {"Address": "4580 S 2300 E", "City": "Holladay", "State": "UT", "Zip": "84117", "Deadline": "10:30 AM", "Weight": "2"},
    "35": {"Address": "1060 Dalton Ave S", "City": "Salt Lake City", "State": "UT", "Zip": "84104", "Deadline": "EOD", "Weight": "88"},
    "36": {"Address": "2300 Parkway Blvd", "City": "West Valley City", "State": "UT", "Zip": "84119", "Deadline": "EOD", "Weight": "88"},
    "37": {"Address": "410 S State St", "City": "Salt Lake City", "State": "UT", "Zip": "84111", "Deadline": "10:30 AM", "Weight": "2"},
    "38": {"Address": "410 S State St", "City": "Salt Lake City", "State": "UT", "Zip": "84111", "Deadline": "EOD", "Weight": "9"},
    "39": {"Address": "2010 W 500 S", "City": "Salt Lake City", "State": "UT", "Zip": "84104", "Deadline": "EOD", "Weight": "9"},
    "40": {"Address": "380 W 2880 S", "City": "Salt Lake City", "State": "UT", "Zip": "84115", "Deadline": "10:30 AM", "Weight": "45"}
}

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.delivered = False
        self.delivery_time = None

    def get_address(self):
        return self.address