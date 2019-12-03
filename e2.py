


import zipfile

zile=zipfile.ZipFile('file.zip',mode='r')
passfile=open('passlist.txt')

for line in passfile.readlines():
	try:
		password=line.strip('\n')
		zile.extractall(pwd=bytes(password))
		print '-------found-----'+'\n'
		print '[+]pass='+password+'\n'
		break
	except Exception, e:
		print'[-]pass='+password+'\n'
