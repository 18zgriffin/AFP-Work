#input of sequence
dnaSequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#counts the total length of the sequence
lengthSequence = len(dnaSequence)

#count the number of C's and G's in the sequence
numG = dnaSequence.count("G")
print("There are", numG, "G's")
numC = dnaSequence.count("C")
print("There are", numC, "C's")

#find the percentage which is G's and percentage which is C's and prints
percentNumg = 100/lengthSequence*numG
print("The percentage which is G is", percentNumg)
percentNumc = 100/lengthSequence*numC
print("The percentage which is C is", percentNumc)

#find the total GC content by adding G and C percentages together and prints it unrounded
totalGccontent = percentNumg+percentNumc
print("The unaltered total G/C content is", totalGccontent)

#rounds to 2 decimal points and prints
totalGccontent2dp = ("%.2f" % totalGccontent)
print("The rounded total is", totalGccontent2dp)
print("The rounded total is also", round(totalGccontent, 2))