# -- coding: utf-8 --
str='hello world'
print str
print str[0]
print str[2:5]
print str[2:]
print str*2
print str+'TEST'

list=['i',12,'love',1.2]
tinylist=[123,"john"]
print list
print list[0]
print list[0:2]
print list[2:]
print tinylist*2
print list+tinylist

dict={}
dict['one']="this is one"
dict[2]="this is two"
tinydict={'name':'john',"code":456,"dept":"sales"}
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
# if语句
flag=False
name="python"
if name=="python":
    flag=True
    print 'welcome boss'
else:
    print name
# while 循环
count=1
while(count<5):
    print "this count is:",count
    count=count+1
print "bye"
# for 循环
for i in 'love':
    print "当前",i
tru=['balala','apple',"color"]
for t in tru:
    print "当前显示",t
print 'bye'
# 引入时间
import time;
ticks=time.time()
print "当前时间是:",ticks

import time
localtime=time.asctime(time.localtime(time.time()))
print "本地时间为:",localtime

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return ;
# 调用函数
printme("我要调用用户自定义函数")
printme("我再次调用同一函数")

# 异常处理
try:
    fh=open('testfile','w')
    fh.write("这是一个测试文件,用于测试异常")
except IOError:
    print "Error:没有找到"









