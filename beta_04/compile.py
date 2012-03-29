#Repace Dirs with a meaningfull command when I get back to my room.

from os import popen3

def main():
    fi,fo,fe = popen3("dir")
    for i in fe.readlines():
        print "error> ",i
    for i in fo.readlines():
        print 'stdout> ',i,

if __name__ == '__main__':
    main()
