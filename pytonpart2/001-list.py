list1=[]

#Lista elem hozzá adása
list1.append(100)
list1.append(101)
list1.append(102)
list1.append(103)
list1.append(104)
list1.append(105)


print(list1)
#Akár szöveges elemet is hozzá lehet adni
list1.append("Eniko")
list1.append("Eniko")
list1.append("Anna")

print(list1)

#Elem törlése a listábol
list1.remove("Eniko")

print(list1)

#Lista törlése telejsen üres listát kapunk

#list1.clear()

#Elem hozzá adása,Két adatot vár el hova szeretnék az adót elemet be szurni és mi az adott elem
list1.insert(5,"Bözsi")

print(list1)

#Lista meg forditása

list1.reverse()

print(list1)

list2=[43,3,65,333,21,12,506]
list2.sort()

print(list2)
#A lista hossza parancs
print(len(list2))