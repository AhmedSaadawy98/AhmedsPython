name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
hand = open(name)
D=dict()

for h in hand:
    h=h.rstrip()
    h=h.split()
    if len(h)<3 or h[0]!='From':continue
    D[h[1]]=D.get(h[1],0)+1
L=-1
mail=None
for k,v in D.items():
    if v > L:
        L=v
        mail=k
print("the most sent mail from",mail,L)
    
