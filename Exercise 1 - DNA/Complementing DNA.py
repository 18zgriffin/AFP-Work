dnaSequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#replaces current A's and C's with placeholder lowercase letters then converts them back to uppercase then prints
dnaSequence = dnaSequence.replace("A", "c")
dnaSequence = dnaSequence.replace("C", "a")
print(dnaSequence)
dnaSequence = dnaSequence.replace("c", "C").replace("a", "A")
print(dnaSequence)

#replaces current G's and T's with placeholder lowercase letters then converts them back to uppercase then prints
dnaSequence = dnaSequence.replace("G", "t")
dnaSequence = dnaSequence.replace("T", "g")
print(dnaSequence)
dnaSequence = dnaSequence.replace("t", "T").replace("g", "G")
print(dnaSequence)