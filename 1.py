import string
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

transfun = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab') 

print text.translate(transfun)
print 'map'.translate(transfun) 