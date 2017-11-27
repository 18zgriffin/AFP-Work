#asks for input of a sentence with space inbetween letters then splits given sentence into a list and prints
words = []
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
print("Your sentence in a list is", words)

#asks for input of letters seperated by commas then splits them into a list and prints
points = []
gamePoints = input("Input the points for each game played eg. 5,6,7,8: ")
points = gamePoints.split(",")
print("The scores in a list is", points)

#adds up the score and then prints the total score made
total = 0
for x in points:
    total += int(x)
print("The score added up is", total)