import os


f=file('test.txt','a')

f.write('hello world     !\n')

f.close()

f=file('test.txt','r')

print f.read()
f.close()


print dir(os)
