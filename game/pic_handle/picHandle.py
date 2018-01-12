from PIL import Image


def addAlpha(src,res):
	img = Image.open(src)
	img = img.convert("RGBA")
	datas = img.getdata()
	newData = list()
	for item in datas:
	    if item[0] >220 and item[1] > 220 and item[2] > 220:
	        newData.append(( 255, 255, 255, 0))
	    else:
	        newData.append(item)

	img.putdata(newData)
	img.save(res,"PNG")

def sizeAdjust(src,res):
	infile = src
	outfile = res
	im = Image.open(infile)
	(x,y) = im.size
	x_s = 100
	y_s = y*x_s/x
	out=im.resize((x_s,y_s),Image.ANTIALIAS)
	out.save(outfile)


addAlpha("./symbol.jpg","./symbol.png")
# addAlpha("../water_red/2.jpg","../water_red/2.png")
# addAlpha("../water_red/3.jpg","../water_red/3.png")
# addAlpha("../water_red/4.jpg","../water_red/4.png")

sizeAdjust("./symbol.png","./symbol.png")
# sizeAdjust("../water_red/2.png","../water_red/2.png")
# sizeAdjust("../water_red/3.png","../water_red/3.png")
# sizeAdjust("../water_red/4.png","../water_red/4.png")
# choice = raw_input("a for addAlpha , b for sizeAdjust  : ")

# if(choice == 'a'):
# 	src = raw_input("src file: ")
# 	res = raw_input("res file: ")
# 	addAlpha(src,res)
# elif(choice == 'b'):
# 	src = raw_input("src file: ")
# 	res = raw_input("res file: ")
# 	sizeAdjust(src,res)