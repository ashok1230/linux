class copy:
    def __init__(self,source,dest):
	self.source=source
	self.dest=dest
	ope=open(self.source,'r')
	data=ope.read()
	ope.close()
	ope=open(self.dest,'w')
	ope.write(data)
	ope.close()
class cat:
    def __init__(self,file):
	self.name=file
	print "if you want to view file data press 1"
	print 'if u want to insert data then press 2'
	print 'if u want to append data then press 3'
	ch=int(raw_input("enter your choice"))
	if ch==1:
	    op=open(self.name,'r')
	    data=op.read()
	    print data
	elif ch==2:
	    print "enter data quit to end"
	    op=open(self.name,'w')
	    while True:
	        data=raw_input()
		if data=='quit':
		    break
		else:
	    	    op.write(data)
		    op.write('\n')
	else:
	    print 'enter data quit to end'
	    op=open(self.name,'a')
	    while True:
                data=raw_input()
		if data=='quit':
		    break
		else:
	            op.write(data)
		    op.write('\n')
class grep:
    def __init__(self,fil,word):
	self.name=fil
	self.word=word
	op=open(self.name,'r')
	data=op.read()
	lst=data.splitlines()
	print lst
	for i in lst:
	    if i.find(self.word)==-1:
		pass
	    else:
		print i
class sort:
    def __init__(self,file):
	self.file=file
	ope=open(self.file,'r')
	data=ope.read()
	lst=data.splitlines()
	for i in range(0,len(lst)):
	    for j in range(i,len(lst)):
		if lst[i]>lst[j]:
		    temp=lst[i]
		    lst[i]=lst[j]
		    lst[j]=temp
	for i in lst:
	    print i

class tail:
    def __init__(self,file,number):
	self.name=file
	self.line=number
	ope=open(self.name,'r')
	data=ope.read()
	lst=data.splitlines()
	#print lst
	count=data.count('\n')
	#print count
	temp=count-self.line
	for i in lst:
	    if lst.index(i)<temp:
		pass
	    else:
		print i
			   
class wc:
    def __init__(self,file):
	self.file=file
	print """if you want number of lines then type 'l'
if you want number of words type 'w'
if you want number of characters type 'c' """
	choice=raw_input("enter your choice :")
	ope=open(self.file,'r')
	data=ope.read()
	count=0
	if choice=='l':
	    lines=data.splitlines()
	    for i in lines:
		count+=1
	elif choice=='c':
	    lines=list(data)
	    for i in lines:
		count+=1
	elif choice=='w':
	    lines=data.split( )
	    for i in lines:
		count+=1	
	else:
	    print 'wrong choice'
	print count  

class head:
    def __init__(self,file,line):
	self.file=file
	self.line=line
	fp=open(self.file,'r')
	data=fp.read()
	lst=data.splitlines()
	for i in lst:
	    if lst.index(i)<self.line:
	        print i
	    else:
		break



