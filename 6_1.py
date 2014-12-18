import zipfile

zzz = zipfile.ZipFile('channel.zip','r')
filestr = '90052'
comment = []
for i in range(1000):
  fname = filestr + ".txt"
  for j in zzz.infolist():
    if j.filename == fname :
      print j.comment
      comment.append(j.comment)
      break
  inzzz = zzz.open(fname).read()
  print 'fname = ' + fname
  print 'inzzz = ' + inzzz
  try:
    filestr = inzzz.split('is ')[1].split('\n')[0] 
  except IndexError:
    print " ".join(comment)
    break

#zzz.read()
