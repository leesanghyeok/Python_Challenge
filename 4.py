import urllib
def urlread(url):
  return urllib.urlopen(url).read()

urlbase = "http://pythonchallenge.com/pc/def/linkedlist.php"
urlstr = urlread(urlbase)
print "urlstr = " + urlstr
url = urlbase + urlstr.split("linkedlist.php")[1].split('">')[0]
#8022
#63579
url = urlbase + "?nothing=63579"
print "url = " + url
urlstr = urlread(url)
print "urlstr = " + urlstr
for i in range(400):
  url = urlbase + "?nothing=" + urlstr.split("is ")[1]
  print "url = " +url
  urlstr = urlread(url)
  print "urlstr = " + urlstr
