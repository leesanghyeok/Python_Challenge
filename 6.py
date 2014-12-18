import zipfile

filepath = "channel/"
filename = filepath+ "90052" + ".txt"
print "filename = " + filename
filestr = open(filename,'r').read()
print "filestr = " + filestr 
for i in range(1):
  filename = filepath + filestr.split("is ")[1].split('\n')[0] + ".txt"
  print str(i) + "filename = " + filename
  filestr = open(filename,'r').read()
  print str(i) + "filestr = " + filestr 

from os import listdir
dirlist = listdir('channel/')
comlist = []
for i in dirlist:
  comlist.append(i+' = '+open(filepath+i,'r').read())

for i in comlist:
  print i
