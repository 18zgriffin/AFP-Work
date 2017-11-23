dnaSequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#finds the length of the sequence and then finds and prints the start location of the recognition site
length = len(dnaSequence)
locale = dnaSequence.find("GAATTC")
print("The recognition site starts at", locale)

split1 = dnaSequence[0:(locale+1)]
split2 = dnaSequence[(locale+1):length]
print("The first part of the sequence is", split1)
print("The second part of the sequence is", split2)

lengthSplit1 = len(split1)
lengthSplit2 = len(split2)
print("The length of the first part is", lengthSplit1, "and the length of the second is", lengthSplit2)