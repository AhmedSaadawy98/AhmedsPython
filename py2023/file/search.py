# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
average=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count+=1
    flt_no=line.find('0.')
    num=float(line[flt_no:])
    total+=num
try:
    print("Average spam confidence:",total/count)
except count==0:
    print("float numbers not found.")