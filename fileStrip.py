#Adjust LLP mathematica ouput to something usable for Yue
#March 24, 2020
#Paul Smith

#file stuff
fname = input('Enter the file name: ')
fout = open('PhiEventsModV6.txt', 'w')

try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()

count = 0
for line in fhand:
	count = count + 1
	#if count >= 6792:
	#	break
	newLine = line.rstrip()
	newLine = newLine.strip('\"')
	newLine = " ".join(newLine.split()[1:])
	#print(newLine)

	if count == 1: 
		newLine = newLine + '\n'
		fout.write(newLine)
		continue
	#mK - mPi = 0.3541
	kinCheck = float(newLine.split()[0])
	if kinCheck > 0.3541:
		continue
	print(kinCheck)
	newLine = newLine + '\n'
	fout.write(newLine)

print('Line Count:', count)