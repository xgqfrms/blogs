#!/usr/bin/env python

# -*- coding:utf-8 -*-
#*********************************************************
#*     暴力字典生成器                                                                                            *
#*  支持自定位数生成，包括大小写字母、特殊符号和数字                     *
#*  BY：netcat  2012-02-10                        *
#* http://www.netcat.tk                           *
#*********************************************************
 
import sys,string,itertools
 
def help():
    print '[usage]: python mydic.py -h or --help to get help\n'
    print '[usage]: python mydic.py mim max outfile\n'
    print '   mim:     mim dic length,must be a number\n'
    print '   max:     max dic length,must be a number\n'
    print 'outfile:    output filename'
 
def dic():
    chars=string.printable[:-5]
    p=[]
    for i in xrange(min,max+1):
        p.append((itertools.product(chars,repeat=i),))
 
    return itertools.chain(*p)
 
def write():
    f=open(file,'a')
    for x in d:
        for y in x:
            f.write("".join(y))
            f.write('\n')
 
    f.close()
    print 'Done'
 
while True:
    if len(sys.argv)==4:
        try:
            min=int(sys.argv[1]);max=int(sys.argv[2])
        except:
            help()
            sys.exit(1)
        if min <= max:
            d=dic()
            file=sys.argv[3]
            write()
            sys.exit(0)
        else:
            print 'error:'+sys.argv[2]+'<'+sys.argv[1]
            sys.exit(1)
    elif len(sys.argv)==2:
        if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "--help":
            help()
            sys.exit(0)
    else:
        help()
        sys.exit(1)



