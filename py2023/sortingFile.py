fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    lineList=line.split()
    for i in range(len(lineList)):
        if lineList[i] not in lst:
            lst.append(lineList[i])
lst.sort()
print(lst)
