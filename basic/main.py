import codecs

lhommequirit_file = codecs.open('../txt/hugo_lhommequirit.txt', 'r', 'utf-8')
lhommequirit_txt = lhommequirit_file.readlines()[51:]

for i in range (10):
	print lhommequirit_txt[i]
