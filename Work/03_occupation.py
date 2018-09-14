# openFire - William Lu, Jiajie Mai
# SoftDev1 pd7
# K06 -- StI/O: Divine your Destiny!
# 2018-09-14

#props to Liang for helping me

#imports random and csv
import random, csv

#sets the resources up, sets up a reader and such
source = open('occupations.csv', 'rU')
reader = csv.reader(source)
reader.next()

#traverses through the reader and makes each a line
dict = {}
for line in reader:
	#print(line, '\n')
	dict[line[0]] = float(line[1])
dict.pop('Total')
#print(dict)

#gets a random number to be the result, traverses through the list and adds the percentages to act as the key finder. If sum is more than or equal to the result, than that is the key and the appropriate key from the dictionary is called
def getKey(dict):
	result = random.random() * 100
	sum = 0
	for key in dict:
		sum += dict[key]
		if sum >= result:
			return key
print(getKey(dict))
