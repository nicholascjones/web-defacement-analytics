import sys

def trimFile( fName ):
	f = open(fName, "r")
	lines = f.readlines()
	f.close()
	f = open(fName, "w")
	counter = 0
	for line in lines:
		if "colspan" in line:
			print(line)
			counter = 2;
		elif counter == 1:
			f.write(line)
		elif "</tr>" in line and counter == 0:
			counter = 1;
	f.close()
	f = open(fName, "r")
	lines = f.readlines()
	f.close()
	lines = lines[:-1]
	f = open(fName, "w")
	for line in lines:
		f.write(line)
	f.close()
	return

for file in sys.argv[1:]:
	trimFile(file);
