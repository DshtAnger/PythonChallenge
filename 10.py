#coding:utf-8
import re
#http://www.pythonchallenge.com/pc/return/bull.html

#几点学习笔记
#findall方法将独立显示元组内容,列表每一项为每一个局部匹配到的内容
print re.findall(r"[a-z]+(\d+)","fuck57cao23")
#findall方法中使用双重元组时，将在列表每一项中依次显示最外层括号、次外层括号所匹配到的内容
print re.findall(r"([a-z]+(\d+))","fuck57cao23")
#命名组(?P<name>...)给规则...命名为name,反向引用(?P=name)将匹配和name组完全相同的内容
print re.findall(r"(?P<w>\d)(?P=w)*","999887")

print "----------------------------------------------------------------------------------------"

arrary = "1"
#最外层括号显示反向引用部分所匹配到的区域内容，内层定义组名的规则部分显示具体匹配到单个字符内容
pattern = re.compile(r'((?P<w>\d)(?P=w)*)')
print pattern.findall("7758525")
for i in xrange(30):
    arrary = "".join(map(lambda x:"%s%s"%(len(x[0]),x[1]),pattern.findall(arrary)))
print "len(a[30]):",len(arrary)
