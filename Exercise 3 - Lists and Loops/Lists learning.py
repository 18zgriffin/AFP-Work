#asks for input of a sentence with space inbetween letters then splits given sentence into a list and prints
words = []
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
print(words)

#asks for input of letters seperated by commas then splits them into a list and prints
points = []
gamePoints = input("Input the points for each game played eg. 5,6,7,8: ")
points = gamePoints.split(",")
print(points)

