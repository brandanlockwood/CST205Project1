
def getRGB(colorRed,colorGreen,colorBlue):
 file = pickAFile()
 pic = makePicture(file)
 for px in getPixels(pic):
  red=getRed(px)
  green= getGreen(px)
  blue=getBlue
  colorRed.append(red)
  colorGreen.append(green)
  colorBlue.append(blue)




oneRed = []
oneGreen = []
oneBlue = []
getRGB(oneRed,oneGreen,oneBlue)

for number in oneBlue:
 print number



