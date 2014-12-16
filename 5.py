import urllib
import pickle
from os.path  import isfile
def urlread(url):
  return urllib.urlopen(url).read()
def fileread(filename):
  if isfile(filename):
    f = open(filename,'r')
    return f.read()    
  else:
    return "false"
def filewrite(filename,data):
  f = open(filename,'w')
  f.write(data)
filename = "5_text"
fstring = fileread(filename) 

if fstring=="false":
  url = "http://pythonchallenge.com/pc/def/banner.p"
  fstring = urlread(url)
  filewrite(filename,fstring)

llist = pickle.loads(fstring)
llist = pickle.load(open('5_text','r'))
newlist = []
for i in llist:
  for j in i:
    newlist.append(j[0]*j[1])
  newlist.append('\n') 
print "".join(newlist)
