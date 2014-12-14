subint = ord('M')-ord('K')
import sys
import string
lowercase = string.ascii_lowercase
def strChange(mstring,cnt):
  retstr = ""
  for i in mstring:
    chch = lowercase.find(i)
    if chch == -1:
      retstr += i
    else:
      itit = lowercase[(chch+cnt) % 26]
      retstr += itit 
  return retstr
solve = strChange(sys.argv[1],subint)
print(solve)

tm = string.maketrans("koe","KOE")
bbb = sys.argv[1].translate(tm)
llll = ""
for i in sys.argv[1]:
  if i == "m" or i == 'q' or i == 'g' :
    llll += i

print llll
llll = ""
for i in solve:
  if i == "m" or i == 'q' or i == 'g' :
    llll += i

print llll
llll = ""
for i in sys.argv[1]:
  if i == "k" or i == 'o' or i == 'e' :
    llll += i

print llll
llll = ""
for i in solve:
  if i == "k" or i == 'o' or i == 'e' :
    llll += i

print llll
