#defines the function
def aa_content(pS, rC):
    lengthSequence = len(pS) + 1

    # count the number of amino acide
    numa = pS.count(rC)
    print("There are", numa, rC + "'s")

    # find the percentage which is amino acid
    percentNuma = 100 / lengthSequence * numa
    print("The percentage which is amino is", percentNuma)

    # rounds to 2 decimal points and prints
    percentNuma2dp = ("%.2f" % percentNuma)
    print("The rounded total is", percentNuma2dp)
    print("The rounded total is also", round(percentNuma, 2))

#gets the input to be put into the function
proteinSequence = input("Input a protein sequence: ")
residueCode = input("Input a residue code: ")

#runs the function with the two inputs
aa_content(proteinSequence, residueCode)
