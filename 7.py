from PIL import Image
ii = Image.open('oxygen.png')
eqrgb = []
for i in range(0,ii.size[0],7):
  r,g,b,x = ii.getpixel((i,45))
  if r==g==b:
    eqrgb.append(r)

print "".join(chr(i) for i in eqrgb)

real = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(chr(i) for i in real)
