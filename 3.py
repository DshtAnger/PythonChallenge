
text = __import__("urllib").urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()

print "".join(__import__("re").findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",text))

print "".join(__import__("re").findall(r"(?<=[^A-Z][A-Z]{3})([a-z])(?=[A-Z]{3}[^A-Z])", text))
