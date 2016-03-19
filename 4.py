import urllib,re
num = "63579"
record = 0
while 1:
    html = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+num).read()
    record = num
    num = "".join(re.findall(" (\d+)",html))    
    print html
    if num=="":
        break
#peak.html

