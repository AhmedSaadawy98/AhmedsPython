#largest = None
#smallest = None
#while True:
#    num = input("Enter a number: ")
#    if num == "done":
#        break
#    try:
#        num=int(num)
#        if smallest is None or smallest>num:
#            smallest=num
#        if largest is None or largest<num:
#            largest=num
#    except ValueError:
#        print("Invalid input")    
#print("Maximum is", largest)
#print("Minimum is", smallest)

#the next code do same thing but make more memory

ilist=list()
while True:
    num = input("Enter a number: ")
    if num == "done":break
    try:
        num=float(num)
        ilist.append(num)
    except ValueError:
        print("Invalid input")    
print("Maximum is", max(ilist))
print("Minimum is", min(ilist))
print("Average is", sum(ilist)/len(ilist))
