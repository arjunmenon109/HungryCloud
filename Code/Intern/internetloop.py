import urllib
intcheck=0
i = 0
for i in 0
    try :
        stri = "https://www.google.co.in"
        data = urllib.urlopen(stri)
        intcheck = 1
    except:
        intcheck = 0
    print(intcheck)
