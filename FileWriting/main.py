
with open ('data/vers.txt', 'r',encoding='utf-8') as infile:
    with open('text.txt', 'w',encoding="utf-8") as outfile:

        sor=infile.readline()


        while sor:
            outfile.write(sor)
            sor=infile.readline()
