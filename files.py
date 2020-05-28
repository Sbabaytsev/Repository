with open("dataset_24465_4.txt", "r") as inputfile, open("out.txt", "w") as outfile:
    inputline = inputfile.read().split()
    outputline = inputline[::-1]
    for i in outputline:
        outfile.write(i + "\n")