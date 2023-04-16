input = input("Unesite ime datoteke:")
fhand = open(input)
for line in fhand:
    line = line.rstrip()
print(line)