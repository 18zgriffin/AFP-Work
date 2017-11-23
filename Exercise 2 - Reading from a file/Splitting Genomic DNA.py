#opens all needed files
file = open("genomic_dna.txt")
intronFile = open("Intron.txt", "w")
exonFile = open("Exons.txt", "w")

#assigns main file data to a variable
dnaSequence = file.read()

#calcualate the length of the sequence
lengthSequence = len(dnaSequence)+1


#finds both exons and prints them
exon1 = dnaSequence[0:63]
exon2 = dnaSequence[91:lengthSequence]
print("Exon 1 is", exon1)
print("Exon 2 is", exon2)

#finds the intron and then prints it
intron = dnaSequence[64:90]
print("The intron is", intron)

#writes exon and introns to their appropriate files
intronFile.write(intron)
exonFile.write(exon1)
exonFile.write("\n")
exonFile.write(exon2)

