#opens all needed files
mainFile = open("ex3-1_input.txt")
trimmedFile = open("trimmed_sequences.txt", "w")

for line in mainFile:
    lineLength = len(line)
    trimmedLine = line[14:lineLength]

    print(trimmedLine)
    print("The trimmed line is", len(trimmedLine), "values long")

    trimmedFile.write(trimmedLine)
    trimmedFile.write("\n")

trimmedFile.close()
mainFile.close()