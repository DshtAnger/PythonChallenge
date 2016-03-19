#coding:utf-8
import zipfile,re
##################reference####################
#   http://www.jb51.net/article/42628.html    #
#   http://www.xuebuyuan.com/2170983.html     #
#   http://wenku.it168.com/d_000647987.shtml  #
###############################################

f = zipfile.ZipFile("channel.zip","r")
currentFileName = "90052.txt"
result = []
while 1:
    text = f.read(currentFileName)
    result.append(f.getinfo(currentFileName).comment)
    print "[+]Reading file :",currentFileName   
    nextFileName = "".join(re.findall(" (\d+)",text))+".txt"
    if nextFileName==".txt":
        print "[*]",text
        break
    else:
        currentFileName = nextFileName
print "".join(result)

'''
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
'''


