##########################################
#Amanda Davis
# Student ID: 001009899
##########################################

import packages
import data
import hashTable

#######################################


#delivery method to make sure packages are delivered on time and on the right truck
#truck 1 (early delivery packages)
    #put package ID not package object
#truck 2 (delay until 9:05)
#truck 3 (wrong address)
#make sure packages are delivered before their timeline
#######################################

#truck info
# load the packages on the trucks manually
#Big O for these: O(1)
truck1 = [1, 8, 13, 14, 15, 16, 19, 20, 21, 30]
truck2 = [3, 4, 5, 6, 7, 10, 11, 12, 18, 29, 31, 34, 36, 37, 38, 40]
truck3 = [2, 9, 17, 22, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39]



######################################################################
packageHourTable = hashTable.HashTable()
packageMinTable = hashTable.HashTable()
tStH = hashTable.HashTable()
tStM = hashTable.HashTable()


#manually inserting each package into hash table
#Big O notation for insertion is best O(1)/ worst O(n)
ht = hashTable.HashTable()
ht.insert(1, packages.p1)
ht.insert(2, packages.p2)
ht.insert(3, packages.p3)
ht.insert(4, packages.p4)
ht.insert(5, packages.p5)
ht.insert(6, packages.p6)
ht.insert(7, packages.p7)
ht.insert(8, packages.p8)
ht.insert(9, packages.p9)
ht.insert(10, packages.p10)
ht.insert(11, packages.p11)
ht.insert(12, packages.p12)
ht.insert(13, packages.p13)
ht.insert(14, packages.p14)
ht.insert(15, packages.p15)
ht.insert(16, packages.p16)
ht.insert(17, packages.p17)
ht.insert(18, packages.p18)
ht.insert(19, packages.p19)
ht.insert(20, packages.p20)
ht.insert(21, packages.p21)
ht.insert(22, packages.p22)
ht.insert(23, packages.p23)
ht.insert(24, packages.p24)
ht.insert(25, packages.p25)
ht.insert(26, packages.p26)
ht.insert(27, packages.p27)
ht.insert(28, packages.p28)
ht.insert(29, packages.p29)
ht.insert(30, packages.p30)
ht.insert(31, packages.p31)
ht.insert(32, packages.p32)
ht.insert(33, packages.p33)
ht.insert(34, packages.p34)
ht.insert(35, packages.p35)
ht.insert(36, packages.p36)
ht.insert(37, packages.p37)
ht.insert(38, packages.p38)
ht.insert(39, packages.p39)
ht.insert(40, packages.p40)
############################################


#nearest neighbor looping

#truck1/2/3 is at hub address
#create outer loop that continues until truck1 list empty
     #create a loop that will go through all packages of truck1
        #find distance from truck1 address to package address
        #is the current distance the smallest distance so far in loop
        #if true remember distance and packageID (loop all the way through all packages)
    #update truck1 address at shortest package address
    #remove packageID from truck1 list
    #update timestamp of package that was delivered
#truck1 returns back to hub

##########################################
#current Location of Truck1
#start time 8 AM
truck1StartH = int(8)
truck1StartM = int(0.0)
truck1CurrH = truck1StartH
truck1CurrM = truck1StartM
#####################################

##BIG O NOTATION FOR NEAREST NEIGHBOR ALGOR: 2 NESTED LOOPS = O(n^2). For all three trucks individually
#starting at hub
currentLocation1 = 0
truckTraveled1 = 0.0
while len(truck1) > 0:
    print("truck1.size:", len(truck1))
    minDist = 100.0
    pkgIndex = 0
    i = 0
    pkgID = 0
    newLocation = 0
    for p in truck1:
        pkg = ht.lookup(p)
        #print("Package #: ", pkg)
        #print("Package address: ", pkg[1])
        destination = data.address_dist[pkg[1]]
        #print("D = ", destination, " CL = ", currentLocation1)
        distance = (data.dist_data[currentLocation1][destination])
        if (minDist > distance):
            minDist = distance
            pkgIndex = i
            pkgID = pkg[0]
            #print("minDist = ", minDist)
            newLocation = destination
        i = i+1
    truck1.pop(pkgIndex)
    min = (10 * minDist)/3
    truck1CurrM += min

    #Big O notation: O(n) for a while loop
    while truck1CurrM >= int(60):
        truck1CurrH += 1
        truck1CurrM -= int(60)
    #print("Removed package#: p", pkgID)
    print("Package ", pkgID, "delivered at: ", truck1CurrH, ":", int(truck1CurrM))
    tStH.insert(pkgID, truck1StartH)
    tStM.insert(pkgID, truck1StartM)
    packageHourTable.insert(pkgID, truck1CurrH)
    packageMinTable.insert(pkgID, truck1CurrM)
    currentLocation1 = newLocation
    #print("New Location is: ", currentLocation1)
    truckTraveled1 = truckTraveled1 + minDist
    print("Total travelled distance: ", truckTraveled1)

truckTraveled1 = truckTraveled1 + currentLocation1
min = (10 * currentLocation1) / 3
truck1CurrM += min
#Big O notation: O(n) for a while loop
while truck1CurrM >= 60:
    truck1CurrH += 1
    truck1CurrM -= 60
#showing time that driver arrives back at hub since this driver will be used for truck 3
print("Total distance of truck1 at hub: ", truckTraveled1, "Arrival at Hub: ", truck1CurrH, ":", int(truck1CurrM))
currentLocation1 = 0 #returned back to hub location
###########################################################

##BIG O NOTATION FOR NEAREST NEIGHBOR ALGOR: 2 NESTED LOOPS = O(n^2). For all three trucks individually

#truck 2 loop
#start time 9:06 AM
truck2StartH = int(9)
truck2StartM = int(6.0)
truck2CurrH = truck2StartH
truck2CurrM = truck2StartM
#################################
#current Location of Truck2
currentLocation2 = 0
truckTraveled2 = 0.0
while len(truck2) > 0:
    print("truck2.size:", len(truck2))
    minDist = 100.0
    pkgIndex = 0
    i = 0
    pkgID = 0
    newLocation2 = 0
    for p in truck2:
        pkg = ht.lookup(p)
        #print("Package #: ", pkg)
        #print("Package address: ", pkg[1])
        destination = data.address_dist[pkg[1]]
        #print("D = ", destination, " CL = ", currentLocation2)
        distance = (data.dist_data[currentLocation2][destination])
        if (minDist > distance):
            minDist = distance
            pkgIndex = i
            pkgID = pkg[0]
            #print("minDist = ", minDist)
            newLocation2 = destination
        i = i+1
    truck2.pop(pkgIndex)
    min = (10 * minDist) / 3
    truck2CurrM += min

    # Big O notation: O(n) for a while loop
    while truck2CurrM >= 60:
        truck2CurrH += 1
        truck2CurrM -= 60
    #print("Removed package#: p", pkgID)
    print("Package ", pkgID, "delivered at: ", truck2CurrH, ":", int(truck2CurrM))
    tStH.insert(pkgID, truck2StartH)
    tStM.insert(pkgID, truck2StartM)
    packageHourTable.insert(pkgID, truck2CurrH)
    packageMinTable.insert(pkgID, truck2CurrM)
    currentLocation2 = newLocation2
    #print("New Location is: ", currentLocation2)
    truckTraveled2 = truckTraveled2 + minDist
    print("Total travelled distance: ", truckTraveled2)

truckTraveled2 = truckTraveled2 + currentLocation2
print("Total distance of truck2 at hub: ", truckTraveled2)
currentLocation2 = 0 #returned back to hub location
##################################################################

##BIG O NOTATION FOR NEAREST NEIGHBOR ALGOR: 2 NESTED LOOPS = O(n^2). For all three trucks individually

#truck3 loop
#current Location of Truck3
#start time of 10 AM
truck3StartH = int(10)
truck3StartM = int(0.0)
truck3CurrH = truck3StartH
truck3CurrM = truck3StartM

#making sure truck 3 is available for the driver to start and back from truck 1
if truck3CurrH <= truck1CurrH:
    if truck3CurrH < truck1CurrH or truck3CurrM < truck1CurrM:
        truck3CurrH = truck1CurrH
        truck3CurrM = truck1CurrM

currentLocation3 = 0
truckTraveled3 = 0.0
while len(truck3) > 0:
    print("truck3.size:", len(truck3))
    minDist = 100.0
    pkgIndex = 0
    i = 0
    pkgID = 0
    newLocation3 = 0
    for p in truck3:
        pkg = ht.lookup(p)
        #print("Package #: ", pkg)
        #print("Package address: ", pkg[1])
        destination = data.address_dist[pkg[1]]
        #print("D = ", destination, " CL = ", currentLocation3)
        distance = (data.dist_data[currentLocation3][destination])
        if (minDist > distance):
            minDist = distance
            pkgIndex = i
            pkgID = pkg[0]
            #print("minDist = ", minDist)
            newLocation3 = destination
        i = i+1
    truck3.pop(pkgIndex)
    min = (10 * minDist) / 3
    truck3CurrM += min

    # Big O notation: O(n) for a while loop
    while truck3CurrM >= 60:
        truck3CurrH += 1
        truck3CurrM -= 60
    #print("Removed package#: p", pkgID)
    print("Package ", pkgID, "delivered at: ", truck3CurrH, ":", int(truck3CurrM))
    tStH.insert(pkgID, truck3StartH)
    tStM.insert(pkgID, truck3StartM)
    packageHourTable.insert(pkgID, truck3CurrH)
    packageMinTable.insert(pkgID, truck3CurrM)
    currentLocation3 = newLocation3
    #print("New Location is: ", currentLocation3)
    truckTraveled3 = truckTraveled3 + minDist
    print("Total travelled distance: ", truckTraveled3)

truckTraveled3 = truckTraveled3 + currentLocation3
print("Total distance of truck3 at hub: ", truckTraveled3)
currentLocation3 = 0 #returned back to hub location
################################################################
#Big O for print is O(1)
#total mileage off all trucks to make sure it is less than 140 miles
total_dist = truckTraveled1 + truckTraveled2 + truckTraveled3
print("Total distance of all trucks: ", total_dist)

####################################################################
#user command line and get them set up for finding a package
#Big O notation: O(n^2) for nest for loop within while loop. If statments doe not change time complexity.

class Main:
    print('Welcome!')
    print('-----------------------')
    print('WGU Package Delivery Program')

cust_input = ''


while cust_input != '6':
    #give options for the command line set up
    print("\n[1] Enter 1 to choose a time to show ALL delivered packages.")
    print("[2] Enter 2 to choose a package to see the status (delivered/en route/at hub.)")
    print("[3] Enter 3 to see total mileage of all the trucks after packages have been delivered.")
    print("[4] Enter 4 to find delivered packages between 2 times.")
    print("[6] Enter 6 to quit.")

    #ask user to choice
    cust_input = input("\nWhat would you like to do?")

    #respond to user
    if cust_input == '1':
        hour = input("\nPlease select the hour(military time).\n")
        minute = input("\nPlease select the minute.\n")
    #create for loop to lookup package ID's in order to show which ones have been delivered at a certain time
        for pkgID in range(1,41):
            h = packageHourTable.lookup(pkgID)
            m = packageMinTable.lookup(pkgID)
            if h != None:
                if int(h) < int(hour) or (int(h)==int(hour) and int(m) <= int(minute)):
                    print(pkgID, " delivered at: ", h, ":", int(m))
        else: print("No package delivered before this time")
#if 2 is choosen the customer will input the package ID and choose a time in order to see if package is en route or delivered or at hub
    elif cust_input =='2':
        pkgID = input("\nPlease enter package ID\n")
        hour = input("\nPlease select the hour(military time)\n")
        minute = input("\nPlease select the minute.\n")

        h = packageHourTable.lookup(int(pkgID))
        m = packageMinTable.lookup(int(pkgID))
        #starting hour time for trucks (lookup)
        hr = tStH.lookup(int(pkgID))
        #starting minute time for trucks lookup
        mi = tStM.lookup(int(pkgID))
        if h != None:
            if int(h) < int(hour) or (int(h) == int(hour) and int(m) <= int(minute)):
                print(pkgID, " delivered at: ", h, ":", int(m))
            elif int(hr) < int(hour) or (int(hr) == int(hour) and int(mi) <= int(minute)):
                print(pkgID, " is loaded on the truck, but still en route at ", int(hour), ":", int(minute))
            elif int(hr) > int(hour) or (int(hr) == int(hour) and int(mi) <= int(minute)):
                print(pkgID, " is still at the hub ", hour, ":", int(minute))

        else:
            print("\nPackage ID not found. Try again. ", pkgID, "\n")
    elif cust_input == '4':
        hourST = input("\nPlease select the first hour(military time).\n")
        minuteST = input("\nPlease select the minute.\n")
        hourEND = input("\nPlease select the second hour(military time).\n")
        minuteEND = input("\nPlease select the minute.\n")
    #create for loop to lookup package ID's in order to show which ones have been delivered at a certain time
        for pkgID in range(1,41):
            h = packageHourTable.lookup(pkgID)
            m = packageMinTable.lookup(pkgID)
            if h != None:
                if (int(h) < int(hourEND) or (int(h)==int(hourEND) and int(m) <= int(minuteEND))) > (int(h) < int(hourST) or (int(h)==int(hourST) and int(m) <= int(minuteST))):
                    print(pkgID, " delivered at: ", h, ":", int(m))
        else:
            print ('No packages delivered in this delivery timeframe. Please try another time')
    #option to exit program altogether
    elif cust_input == '6':
        print("\nExiting WGU Delivery Program.\n")
    elif cust_input == '3':
        print("Total distance of all trucks: ", total_dist, " miles.")
    else:
        print("\nIncorrect input. Please try again.\n")
#
print("Thanks for visiting the WGU Delivery Service. Goodbye.")

