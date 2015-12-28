
def convert_to_num(arg):
    ''' Tries to convert arg to number, from string, if possible.
    '''
    try:
        arg = float(arg)
        # to convert to int when possible
        if arg == int(arg):
            arg = int(arg)
    except:
        pass
    return arg



print "enter key"
arr=[]
dic={}

while(True):
	
	inp=raw_input()
	inp=convert_to_num(inp)
	if type(inp)== str :
		if inp[0]=='(' :
			inp=inp[1:-1].split(',')
			for t in inp:
				n=convert_to_num(t)
				if type(n)!=str:
					inde=inp.index(t)
					inp.remove(t)
					inp.insert(inde,n)
			inp=tuple(inp)
			
	if inp == 'end':
		break

	arr=arr+[inp]
	print arr


print "Enter Values "
for element in arr:
	val=raw_input()
	val=convert_to_num(val)
	if type(val)== str :
		if val[0]=='[' or val[0]=='(':
			val=val[1:-1].split(',')
		
		for v in val:
			l=convert_to_num(v)
			if type(l)!=str:
					inde=val.index(v)
					val.remove(v)
					val.insert(inde,l)

		if val[0]=='(':
			val=tuple(val)
	dic[element]=val

print dic

