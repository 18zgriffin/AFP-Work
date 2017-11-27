#start of code says what it is
print("The code will give you data about your montly rainfall that you may input""\n")

#creates rainfall variable and asks for input, once done it then splits it into a list
rainfall = []
myRainfall = input("Enter the rainfall for each month in mm eg. 25,27,13,56: ")
rainfall = myRainfall.split(",")
print("The rainfalls in list format is", rainfall)

#turns each value in the list into a variable and then sorts highest to lowest
sortRainfall = [int(x) for x in rainfall]
sortRainfall.sort()
print("The rainfall sorted lowest to highest is", sortRainfall)

#finds the highest value and the lowest value
highest = sortRainfall[-1]
lowest = sortRainfall[0]
print("The highest average rainfall was", highest)
print("The lowest average rainfall was", lowest)

#adds all of the values up finding the total
totalRainfall = 0
for x in rainfall:
    totalRainfall += int(x)
print("The total rainfall was", totalRainfall)

#then calculates the average or mean monthly rainfall
listLength = len(rainfall)
averageRainfall = totalRainfall/listLength
print("The average rainfall was", "%.2f" % averageRainfall)
