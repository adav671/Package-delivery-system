#big O notation to define class: O(1)

class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, notes, status, timestamp):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.timestamp = timestamp

    def __getAdd__(self):
        return self.address

#big O for string = O(1)
def __str__(self): #overwrite so it won't print object ref
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes, self.status, self.timestamp)

#add all information on package and include status and timestamp
#big O for array = best case indexing O(1) worst case for searching is O(n)

p1 = (1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30 AM",	21, "", "")
p2 = (2, "2530 S 500 E", "Salt Lake City",	"UT",	84106,	"EOD",	44, "", "", "")
p3 = (3, "233 Canyon Rd", "Salt Lake City", "UT",	84103,	"EOD", 2, "Can only be on truck 2", "", "")
p4 = (4, "380 W 2880 S",	"Salt Lake City",	"UT",	84115,	"EOD",	4, "", "", "")
p5 = (5,	"410 S State St",	"Salt Lake City",	"UT",	84111,	"EOD", 5, "", "", "")
p6 = (6, "3060 Lester St", "West Valley City",	"UT",	84119,	"10:30 AM",	88,	"Delayed arrive at 9:05 am", "", "")
p7 = (7,	"1330 2100 S",	"Salt Lake City",	"UT",	84106,	"EOD",	8, "", "")
p8 = (8,	"300 State St",	"Salt Lake City",	"UT",	84103,	"EOD",	9,	"", "")
p9 = (9,	"410 S State St",	"Salt Lake City",	"UT",	84111,	"EOD",	2,	"Wrong address listed until 10:20", "", "")
p10 = (10, "600 E 900 South", "Salt Lake City",	"UT", 84105, "EOD", 1, "", "", "")
p11 = (11,	"2600 Taylorsville Blvd",	"Salt Lake City",	"UT",	84118,	"EOD",	1, "", "", "")
p12 = (12,	"3575 W Valley Central Station bus Loop", "West Valley City",	"UT",	84119,	"EOD",	1,	"", "", "")
p13 = (13,	"2010 W 500 S",	"Salt Lake City",	"UT",	84104,	"10:30 AM",	2, "", "")
p14 = (14,	"4300 S 1300 E", "Millcreek",	"UT",	84117,	"10:30 AM",	88,	"Must be delivered with 15, 19", "", "")
p15 = (15,	"4580 S 2300 E",	"Holladay",	"UT",	84117,	"9:00 AM",	4, "", "", "")
p16 = (16,	"4580 S 2300 E",	"Holladay",	"UT",	84117,	"10:30 AM",	88,	"Must be delivered with 13, 19", "", "")
p17 = (17,	"3148 S 1100 W",	"Salt Lake City",	"UT",	84119,	"EOD",	2, "", "", "")
p18 = (18,	"1488 4800 S", "Salt Lake City",	"UT",	84123,	"EOD",	6,	"Can only be on truck 2", "", "")
p19 = (19,	"177 W Price Ave",	"Salt Lake City",	"UT",	84115,	"EOD",	37, "", "", "")
p20 = (20,	"3595 Main St",	"Salt Lake City",	"UT",	84115,	"10:30 AM",	37,	"Must be delivered with 13, 15", "", "")
p21 = (21,	"3595 Main St",	"Salt Lake City",	"UT",	84115,	"EOD",	3, "", "", "")
p22 = (22,	"6351 South 900 East",	"Murray",	"UT",	84121,	"EOD",	2, "", "", "")
p23 = (23,	"5100 South 2700 West",	"Salt Lake City",	"UT",	84118,	"EOD",	5, "", "", "")
p24 = (24,	"5025 State St",	"Murray",	"UT",	84107,	"EOD",	7, "", "", "")
p25 = (25,	"5383 S 900 East #104",	"Salt Lake City",	"UT",	84117,	"10:30 AM",	7, "Delayed arrive at 9:05 am", "", "")
p26 = (26,	"5383 S 900 East #104",	"Salt Lake City",	"UT",	84117,	"EOD",	25, "", "", "")
p27 = (27,	"1060 Dalton Ave S",	"Salt Lake City",	"UT",	84104,	"EOD",	5, "", "", "")
p28 = (28,	"2835 Main St",	"Salt Lake City",	"UT",	84115,	"EOD",	7,	"Delayed on flight arrive at 9:05 am", "", "")
p29 = (29,	"1330 2100 S",	"Salt Lake City",	"UT",	84106,	"10:30 AM",	2, "", "", "")
p30 = (30,	"300 State St",	"Salt Lake City",	"UT",	84103,	"10:30 AM",	1, "", "", "")
p31 = (31,	"3365 S 900 W",	"Salt Lake City", "UT",	84119,	"10:30 AM",	1,	"", "", "")
p32 = (32,	"3365 S 900 W",	"Salt Lake City",	"UT",	84119,	"EOD",	1,	"Delayed on flight arrive at 9:05 am", "", "")
p33 = (33,	"2530 S 500 E",	"Salt Lake City",	"UT",	84106,	"EOD",	1, "", "", "")
p34 = (34,	"4580 S 2300 E",	"Holladay",	"UT",	84117,	"10:30 AM",	2, "", "", "")
p35 = (35,	"1060 Dalton Ave S",	"Salt Lake City",	"UT",	84104,	"EOD",	88, "", "", "")
p36 = (36,	"2300 Parkway Blvd",	"West Valley City",	"UT",	84119,	"EOD",	88,	"Can only be on truck 2", "", "")
p37 = (37,	"410 S State St",	"Salt Lake City",	"UT",	84111,	"10:30 AM",	2, "", "", "")
p38 = (38,	"410 S State St",	"Salt Lake City",	"UT",	84111,	"EOD",	9,	"Can only be on truck 2", "", "")
p39 = (39,	"2010 W 500 S",	"Salt Lake City",	"UT",	84104,	"EOD",	9, "", "", "")
p40 = (40,	"380 W 2880 S",	"Salt Lake City",	"UT",	84115,	"10:30 AM",	45, "", "", "")










