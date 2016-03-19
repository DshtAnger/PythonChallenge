#http://www.pythonchallenge.com/pc/return/evil.html
#http://www.xue163.com/154/6/1548606.html
content=open("evil2.gfx").read()
[open("12_%d.jpg" %i, "w").write(content[i::5]) for i in range(5)]

#disproportional