import Image
#referencee:
#           http://hhlux.iteye.com/blog/559345
#           http://www.douban.com/note/237121347             
im = Image.open("oxygen.png")  
print im.format, im.mode, im.size

height = 0
startHeightPosition = 0
endHeightPosition = 0
while 1:
    R,G,B,A=im.getpixel((0,height))
    if R==G==B:
        if startHeightPosition == 0:
            print "[*]Start  height:",height
            startHeightPosition = height
            height +=1
        if startHeightPosition!=0 and endHeightPosition == 0 :
            height += 1   
    else:
        if startHeightPosition!=0 and endHeightPosition == 0 :
            print "[*]End  height:",height
            endHeightPosition = height
            break
        height += 1
width = 0
startWidthPosition = 0
endWidthPosition = 0      
while 1:
    R,G,B,A=im.getpixel((width,43))
    if R==G==B:
        if startWidthPosition == 0:
            print "[*]Start  width:",width
            startWidthPosition = width+1
            width +=1
        if startWidthPosition!=0 and endWidthPosition == 0 :
            width += 1   
    else:
        if startWidthPosition!=0 and endWidthPosition == 0 :
            print "[*]End  width:",width
            endWidthPosition = width
            break
        width += 1

for height in xrange(43,52):
    print ''.join([chr(im.getpixel((width,height))[0]) for width in range(0,608,7)])  

print "".join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))
