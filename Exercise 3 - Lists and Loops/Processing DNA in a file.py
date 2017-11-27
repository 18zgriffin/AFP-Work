#opens all needed files
mainFile = open("ex3-1_input.txt")
trimmedFile = open("trimmed_sequences.txt", "w")

for line in mainFile:
    lineLength = len(line)
    trimmedline = line[14:lineLength]
    print(trimmedline)
    print("The trimmed line is", len(trimmedline), "values long")
    trimmedFile.write(trimmedline)
    trimmedFile.write("\n")