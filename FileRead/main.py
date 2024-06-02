#file=open("vers.txt","r",encoding="utf-8")

#for line in file:
#    print(line.strip())

#file.close()

with open('vers.txt','r',encoding='utf-8') as file:

    for line in file:
        print(line.strip())