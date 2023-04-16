import statistics
lst1 = []
lst2 = []
unos = input("unesite ime datoteke:")
fhand = open(unos)
c=0
for line in fhand:
    if(line.startswith('X-DSPAM-Confidence:')):
        c +=1
        line = line.strip('X-DSPAM-Confidence:')
        lst1.append(float(line))

print("Ime datoteke:", unos)
print("Average X-DSPAM-Confidence:",statistics.mean(lst1))

unos2 = input("unesite ime datoteke:")
fhand2 = open(unos2)
cntr = 0
for line2 in fhand2:
    if(line2.startswith('X-DSPAM-Confidence:')):
        cntr +=1
        line2 = line2.split('X-DSPAM-Confidence:')
        print(line2)
        lst2.append(float(line2))

print("Ime datoteke:", unos2)
print("Average X-DSPAM-Confidence:", statistics.mean(lst2))



        




