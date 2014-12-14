import sys
import urllib
def fileread(filename):
  f = open(filename,'r')
  return f.read()    
def urlread(url):
  return urllib.urlopen(url).read()

fstring = urlread(sys.argv[1]).split("<!--")[2].split('-->')[0]
print fstring
strset = list(set(fstring))
print strset
cpset = strset[:]
#print cpset
for i in strset:
  cc = strset.index(i)
  cpset[cc] = fstring.count(i)

print cpset
newlist = []
for i in strset:
  if fstring.count(i)==1:
    newlist.append(i)
newlist.sort()
print newlist

