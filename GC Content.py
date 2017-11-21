#input of sequence
dnaSequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#counts the total length of the sequence
lengthSequence = len(dnaSequence)

#count the number of C's and G's in the sequence
numG = dnaSequence.count("G")
print(numG)
numC = dnaSequence.count("C")
print(numC)

#find the percentage which is G's and percentage which is C's and prints
percentNumg = 100/lengthSequence*numG
percentNumc = 100/lengthSequence*numC

#find the total GC content by adding G and C percentages together and prints it unrounded
totalGccontent = percentNumg+percentNumc
print(totalGccontent)

#rounds to 2 decimal points and prints
totalGccontent2dp = ("%.2f" % totalGccontent)
print(totalGccontent2dp)
print(round(totalGccontent, 2))