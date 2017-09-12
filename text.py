# -- coding: utf-8 --

# for i in range(1,10):
#     s=""
#     for j in range(1,i+1):
#         # s += str(j) + '*' + str(i) + '=' + '{0:2d}'.format(j * i) + '\t'
#         # s += str(j) + '*' + str(i) + '=' + repr(j * i).ljust(4)
#         s += str(j) + '*' + str(i) + '=' + str(j * i) + '\t'
#     print s

for i in range(1,10):
    for j in range(1,i+1):
            print "%d*%d=%2d" % (i,j,i*j),"",
    if j==i:
        print("")