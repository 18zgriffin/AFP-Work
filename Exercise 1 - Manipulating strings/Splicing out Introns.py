dnaSequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

lengthSequence = len(dnaSequence)+1

#finds both exons and prints them
exon1 = dnaSequence[0:63]
exon2 = dnaSequence[91:lengthSequence]
print("Exon 1 is", exon1)
print("Exon 2 is", exon2)

#finds the length each exon
lengthExon1 = len(exon1)
lengthExon2 = len(exon2)
print("The length of Exon 1 is", lengthExon1, "and the length of Exon 2 is", lengthExon2)

#finds the percentage that each exon is of the total
lengthExon1percent = 100/lengthSequence*lengthExon1
lengthExon2percent = 100/lengthSequence*lengthExon2

#adds exon percentages together and prints is unrounded
exonPercentage = lengthExon1percent+lengthExon2percent
print("The unrouned exon percentage is", exonPercentage)

#prints the exon percentage with 2 decimals points
print("The rounded exon percentage is", "%.2f" % exonPercentage)