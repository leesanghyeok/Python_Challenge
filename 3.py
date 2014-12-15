import urllib
from os.path  import isfile
def fileread(filename):
  if isfile(filename):
    f = open(filename,'r')
    return f.read()    
  else:
    return "false"
def urlread(url):
  return urllib.urlopen(url).read()
def filewrite(filename,data):
  f = open(filename,'w')
  f.write(data)

fstring = fileread("3_text") 
if fstring=="false":
  url = "http://www.pythonchallenge.com/pc/def/equality.html"
  fstring = urlread(url).split("<!--")[1].split('-->')[0]
  filewrite("3_text",fstring)

mstr = ""
for i in range(len(fstring)-2):
  if fstring[i].islower():
    k = 0
    for u in range(1,4):
      if fstring[i+u].isupper() and fstring[i-u].isupper() and (i+u)<len(fstring) and (i-u)>0:
        k = k +1
    if k==3 and fstring[i+4].islower() and fstring[i-4].islower():
        mstr = mstr + fstring[i]
print mstr 

