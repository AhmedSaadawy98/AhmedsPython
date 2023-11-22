fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    line=line.split()
    if len(line)<3 or line[0]!='From':  #the first condition is gardain and it must be first  
        continue
    print(line[1])
    count+=1
print("There were", count, "lines in the file with From as the first word")
