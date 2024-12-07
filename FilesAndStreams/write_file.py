# to create a new file and write something in it

s='subbai'
sh='shirley'
with open("sample.data","a") as fp:
    fp.write(s+'\t')
    fp.write(sh+'\n')
with open("sample.data",'r') as rp:
    readdata=rp.read()
print(readdata)