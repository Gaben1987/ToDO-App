sum=0
n=int(input("Mennyi számbol számoljak átlagot:"))
    
for i in range(1,n+1):
    text="Kérem a(z)"+str(i)+"-ik számot:"
    #Mint a funcionál csak keretes záro jel helyett ketöss pont van
    #Ami után imétlödik a funcio
    num=int(input(text))
    sum=sum+num
    avarages=sum/n
    # Igy lehet kerekiteni számokat
    avarages=round(avarages,2)


print(avarages)