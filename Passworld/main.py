passworld=input("Press Enter to password:")

result=[]
if len(passworld) >8:
    result.append(True)
else:
    result.append(False)

digit=False
for i in passworld:
    if i.isdigit():
        digit=True
result.append(digit)

upper=False
for i in passworld:
    if i.isupper():
        upper=True
result.append(upper)

print(result)

if all(result)==True:
    print('Password is strong!')
else:
    print ('Password is bad!')





