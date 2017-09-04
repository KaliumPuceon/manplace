import re

raw = open("raw.txt","r")
stor = raw.read()
stor = stor.split("\n")
clean = []
for k in stor:
    start = -1
    end = -1
    start = k.find("[[")
    end = k.find("]]")
    if start>0 and end>0:
        print(k[start+2:end:])

raw.close()
