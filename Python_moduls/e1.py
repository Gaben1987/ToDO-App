import glob

myfiles = glob.glob("*.txt")

myfiles_2=glob.glob("files/*.txt")

for file in myfiles_2:
    with open(file,'r') as f:
        print(f.read())

print( myfiles)
print( myfiles_2)