#team purple
#Clara Mohri and Jiajie Mai
#SoftDev1 Pd07
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-08

#massive props to Clara for helping me as I know no Python

import random

KREWES = {
        "w": ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],
        "m": ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],
        "x": ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']}

#printBuddy() prints the name of a randomly-selected student from team (w, m, or x).
def printBuddy():
    #create list with all possible keys
    list = ["w", "m", "x"]
    #choose random key from possibe keys, and store this key in key
    key = random.choice(list)
    #identify the corresponding val to key and store in val
    val = KREWES[key]
    #choose random name from val, and call it buddy
    buddy = random.choice(val)
    #print buddy's name
    print(buddy)

printBuddy()
