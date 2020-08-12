
"""
print(ord("e")) #ord converts to ---->asci numbers 
print(ord("\n"))
print(ord('e'),ord('e'),ord('e'),ord('e'))
"""
"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())

"""

"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().split() # strip will give alphabets 
    for word in words: 
        counts[word] = counts.get(word,0) + 1
print(counts)
"""


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Kylian.html")

counts = dict()
for line in fhand:
    words = line.decode().split() # strip will give alphabets 
    for word in words: 
        counts[word] = counts.get(word,0) + 1
print(counts)



