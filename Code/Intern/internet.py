import urllib
try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri)
    print "Connected"
except:
    print "not connected" 