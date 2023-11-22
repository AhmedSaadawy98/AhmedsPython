ifile=input('Enter file name :')
try:
    xfile=open(ifile)
except:
    print("File you enter ",ifile,"invalid.")
    quit()
count=0
word=input('Enter the word start of the line you want to see:')
for line in xfile:
    if line.startswith(word):
        count+=1
print("there is",count,"lines start with word you entered")
