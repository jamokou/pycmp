# Program Name : pycmp
# Programmer   : The Alpha
# Credits      : Iranpython.blog.ir
# Version      : 0.9(Beta Version)
# Linted By    : Pyflakes
# Info         : pycmp is a simple terminal-based program written in pure python
# that uses to check a bunch of files for detecting similarity in words used  in
# those files. Of course this is a BETA VERSION and has some bugs I'm      still
# working on it to patch bugs.

import sys
import os

scriptName, file1, file2 = sys.argv

fh1 = open(sys.argv[1])
data1 = str(fh1.readlines())
fh1.close()

fh2 = open(sys.argv[2])
data2 = str(fh2.readlines())
fh2.close()

data1 = data1[2:len(data1)-4]
data2 = data2[2:len(data2)-4]
data1 = data1.split(' ')
data2 = data2.split(' ')
similar = []

# BruteForce Algorithm
for word in data1:
	for word2 in data2:         
		if word2 == word:
			similar.append([word, data1.count(word), data2.count(word2)])
			for item in similar:
				if similar.count(item) > 1:
					for time in range(similar.count(item)-1):
						similar.remove(item)

# Query Maker
os.system("cls")

print("\t\t\t\tIn The Name Of Allah\n\n\t\t\t\t Ashiyane PYCMP 0.9\n")
print("[CM]-PYCMP >> Welcome to your PYCMP 0.9 (written by The Alpha)\n")
print("[CM]-PYCMP >> If you see any problem report it at :\n------> http://www.iranpython.blog.ir\n")

if sys.argv[1] != sys.argv[2]:
    print("[CM]-PYCMP >> This Two Files Has {} similar word(s).\n".format(len(similar)))
	
if len(similar)>0:
	print("|"+ "-"*30)
	print("[CM]-PYCMP >> This Words Are : ")
	print("|"+"-"*30)
	for x in range(len(similar)):		
		print(str(x+1)+"." + " #" + similar[x][0] + "#\n\t Used In {file1} : {n1} time(s) |\n\t Used In {file2} : {n2} time(s)".format(
			file1=sys.argv[1], n1=similar[x][1], file2=sys.argv[2], n2=similar[x][2]))			
else :
	print("PYCMP >> This is just one file and there is no difference in word(s) used.")

# Finding words without frequently usage
def real_word_finder(listName):
	for item in listName:
		if listName.count(item) > 1 :
			len_of_list = len(listName)-listName.count(item)+1
			return len_of_list
real_word_finder(data1)
real_word_finder(data2)
