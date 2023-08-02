
#!/usr/bin/env python3
# coding: utf8

__author__ = 'xgqfrms'
__editor__ = 'vscode'
__version__ = '1.0.1'
__github__ = 'https://github.com/xgqfrms/Raspberry-Pi'
__git__ = 'https://github.com/xgqfrms/Raspberry-Pi.git'
__copyright__ = """
  Copyright (c) 2012-2050, xgqfrms; mailto:xgqfrms@xgqfrms.xyz
"""


#*********************************************************
#*     社会工程学字典生成器                                                                                *
#*  根据name，age，birthday，mail，qq等生成密码                      *
#*  BY：netcat  2012-02-10                        *
#* http://www.netcat.tk                           *
#*********************************************************
 
import itertools
 
def input():
    l=[]
    name=raw_input('enter name>')
    l.append(name)
    net_name=raw_input('enter netname>')
    try:
        age=str(int(raw_input('enter age>')))
    except:
        print 'age must be a number.eg:44'
        return input()
    else:
        l.append(age)
    try:
        birthday=str(int(raw_input('enter birthday>')))
    except:
        print 'birthday must be a number.eg:19900304'
        return input()
    else:
        l.append(birthday)
    mail=raw_input('enter mail>')
    l.append(mail)
    try:
        qq=str(int(raw_input('enter qq>')))
    except:
        print 'qq must be number.eg:123321'
        return input()
    else:
        l.append(qq)
    other1=raw_input('enter other1>')
    l.append(other1)
    other2=raw_input('enter other2>')
    l.append(other2)
 
    return l
 
def dic():
    p=[]
    for x in xrange(8):
        p.append((itertools.product([i for i in ans],repeat=x),))
    return itertools.chain(*p)
 
def write():
    file=raw_input('enter dic name>')
    if file == '':
        file='a1.txt'
        print 'create dic file a1.txt'
    f=open(file,'a')
    for x in d:
        for y in x:
            f.write("".join(y))
            f.write('\n')
 
    f.close()
    print 'Done'
 
ans=input()
d=dic()
write()

"""

Kali linux 下破解wifi:

用python写的两个字典生成器:

下面两个是我自己写的字典生成器，代码比较简单，大牛勿笑。

第一个是指定字典的最长和最短，然后盲目生成字典的生成器，包括数字，大小写字母，特殊符号等。



第二个字典也叫社会工程学字典，是根据name，age，birthday，mail等生成字典的生成器。代码如下：

"""
